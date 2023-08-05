# Copyright (c) OpenMMLab. All rights reserved.
import pickle
from copy import deepcopy
from functools import partial

import mmcv
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parallel import DataParallel, DistributedDataParallel
from torch.nn.parallel.distributed import _find_tensors

from mmgen.models.architectures.common import get_module_device
from mmgen.models.builder import MODELS, build_module
from mmgen.models.gans.base_gan import BaseGAN
from ..common import set_requires_grad


@MODELS.register_module()
class SinGAN(BaseGAN):
    """SinGAN.

    This model implement the single image generative adversarial model proposed
    in: Singan: Learning a Generative Model from a Single Natural Image,
    ICCV'19.

    Notes for training:

    - This model should be trained with our dataset ``SinGANDataset``.
    - In training, the ``total_iters`` arguments is related to the number of
      scales in the image pyramid and ``iters_per_scale`` in the ``train_cfg``.
      You should set it carefully in the training config file.

    Notes for model architectures:

    - The generator and discriminator need ``num_scales`` in initialization.
      However, this arguments is generated by ``create_real_pyramid`` function
      from the ``singan_dataset.py``. The last element in the returned list
      (``stop_scale``) is the value for ``num_scales``. Pay attention that this
      scale is counted from zero. Please see our tutorial for SinGAN to obtain
      more details or our standard config for reference.

    Args:
        generator (dict): Config for generator.
        discriminator (dict): Config for discriminator.
        gan_loss (dict): Config for generative adversarial loss.
        disc_auxiliary_loss (dict): Config for auxiliary loss to
            discriminator.
        gen_auxiliary_loss (dict | None, optional): Config for auxiliary loss
            to generator. Defaults to None.
        train_cfg (dict | None, optional): Config for training schedule.
            Defaults to None.
        test_cfg (dict | None, optional): Config for testing schedule. Defaults
            to None.
    """

    def __init__(self,
                 generator,
                 discriminator,
                 gan_loss,
                 disc_auxiliary_loss,
                 gen_auxiliary_loss=None,
                 train_cfg=None,
                 test_cfg=None):
        super().__init__()
        self._gen_cfg = deepcopy(generator)
        self.generator = build_module(generator)

        # support no discriminator in testing
        if discriminator is not None:
            self.discriminator = build_module(discriminator)
        else:
            self.discriminator = None

        # support no gan_loss in testing
        if gan_loss is not None:
            self.gan_loss = build_module(gan_loss)
        else:
            self.gan_loss = None

        if disc_auxiliary_loss:
            self.disc_auxiliary_losses = build_module(disc_auxiliary_loss)
            if not isinstance(self.disc_auxiliary_losses, nn.ModuleList):
                self.disc_auxiliary_losses = nn.ModuleList(
                    [self.disc_auxiliary_losses])
        else:
            self.disc_auxiliary_losses = None

        if gen_auxiliary_loss:
            self.gen_auxiliary_losses = build_module(gen_auxiliary_loss)
            if not isinstance(self.gen_auxiliary_losses, nn.ModuleList):
                self.gen_auxiliary_losses = nn.ModuleList(
                    [self.gen_auxiliary_losses])
        else:
            self.gen_auxiliary_losses = None

        # register necessary training status
        self.curr_stage = -1
        self.noise_weights = [1]
        self.fixed_noises = []
        self.reals = []
        self.train_cfg = deepcopy(train_cfg) if train_cfg else None
        self.test_cfg = deepcopy(test_cfg) if test_cfg else None

        self._parse_train_cfg()
        if test_cfg is not None:
            self._parse_test_cfg()

    def _parse_train_cfg(self):
        """Parsing train config and set some attributes for training."""
        if self.train_cfg is None:
            self.train_cfg = dict()

        # whether to use exponential moving average for training
        self.use_ema = self.train_cfg.get('use_ema', False)
        if self.use_ema:
            # use deepcopy to guarantee the consistency
            self.generator_ema = deepcopy(self.generator)

    def _parse_test_cfg(self):
        if self.test_cfg.get('pkl_data', None) is not None:
            with open(self.test_cfg.pkl_data, 'rb') as f:
                data = pickle.load(f)
                self.fixed_noises = self._from_numpy(data['fixed_noises'])
                self.noise_weights = self._from_numpy(data['noise_weights'])
                self.curr_stage = data['curr_stage']

            mmcv.print_log(f'Load pkl data from {self.test_cfg.pkl_data}',
                           'mmgen')

    def _from_numpy(self, data):
        if isinstance(data, list):
            return [self._from_numpy(x) for x in data]

        if isinstance(data, np.ndarray):
            data = torch.from_numpy(data)
            device = get_module_device(self.generator)
            data = data.to(device)
            return data

        return data

    def get_module(self, model, module_name):
        """Get an inner module from model.

        Since we will wrapper DDP for some model, we have to judge whether the
        module can be indexed directly.

        Args:
            model (nn.Module): This model may wrapped with DDP or not.
            module_name (str): The name of specific module.

        Return:
            nn.Module: Returned sub module.
        """
        if isinstance(model, (DataParallel, DistributedDataParallel)):
            return getattr(model.module, module_name)

        return getattr(model, module_name)

    def sample_from_noise(self,
                          noise,
                          num_batches=0,
                          curr_scale=None,
                          sample_model='ema/orig',
                          **kwargs):
        """Sample images from noises by using the generator.

        Args:
            noise (torch.Tensor | callable | None): You can directly give a
                batch of noise through a ``torch.Tensor`` or offer a callable
                function to sample a batch of noise data. Otherwise, the
                ``None`` indicates to use the default noise sampler.
            num_batches (int, optional):  The number of batch size.
                Defaults to 0.

        Returns:
            torch.Tensor | dict: The output may be the direct synthesized \
                images in ``torch.Tensor``. Otherwise, a dict with queried \
                data, including generated images, will be returned.
        """
        # use `self.curr_scale` if curr_scale is None
        if curr_scale is None:
            curr_scale = self.curr_stage

        if sample_model == 'ema':
            assert self.use_ema
            _model = self.generator_ema
        elif sample_model == 'ema/orig' and self.use_ema:
            _model = self.generator_ema
        else:
            _model = self.generator

        if not self.fixed_noises[0].is_cuda and torch.cuda.is_available():
            self.fixed_noises = [
                x.to(get_module_device(self)) for x in self.fixed_noises
            ]

        outputs = _model(
            None,
            fixed_noises=self.fixed_noises,
            noise_weights=self.noise_weights,
            rand_mode='rand',
            num_batches=num_batches,
            curr_scale=curr_scale,
            **kwargs)

        return outputs

    def construct_fixed_noises(self):
        """Construct the fixed noises list used in SinGAN."""
        for i, real in enumerate(self.reals):
            h, w = real.shape[-2:]
            if i == 0:
                noise = torch.randn(1, 1, h, w).to(real)
                self.fixed_noises.append(noise)
            else:
                noise = torch.zeros_like(real)
                self.fixed_noises.append(noise)

    def train_step(self,
                   data_batch,
                   optimizer,
                   ddp_reducer=None,
                   running_status=None):
        """Train step function.

        This function implements the standard training iteration for
        asynchronous adversarial training. Namely, in each iteration, we first
        update discriminator and then compute loss for generator with the newly
        updated discriminator.

        As for distributed training, we use the ``reducer`` from ddp to
        synchronize the necessary params in current computational graph.

        Args:
            data_batch (dict): Input data from dataloader.
            optimizer (dict): Dict contains optimizer for generator and
                discriminator.
            ddp_reducer (:obj:`Reducer` | None, optional): Reducer from ddp.
                It is used to prepare for ``backward()`` in ddp. Defaults to
                None.
            running_status (dict | None, optional): Contains necessary basic
                information for training, e.g., iteration number. Defaults to
                None.

        Returns:
            dict: Contains 'log_vars', 'num_samples', and 'results'.
        """

        # get running status
        if running_status is not None:
            curr_iter = running_status['iteration']
        else:
            # dirty walkround for not providing running status
            if not hasattr(self, 'iteration'):
                self.iteration = 0
            curr_iter = self.iteration

        # init each scale
        if curr_iter % self.train_cfg['iters_per_scale'] == 0:
            self.curr_stage += 1
            # load weights from prev scale
            self.get_module(self.generator, 'check_and_load_prev_weight')(
                self.curr_stage)
            self.get_module(self.discriminator, 'check_and_load_prev_weight')(
                self.curr_stage)
            # build optimizer for each scale
            g_module = self.get_module(self.generator, 'blocks')
            param_list = g_module[self.curr_stage].parameters()

            self.g_optim = torch.optim.Adam(
                param_list, lr=self.train_cfg['lr_g'], betas=(0.5, 0.999))
            d_module = self.get_module(self.discriminator, 'blocks')
            self.d_optim = torch.optim.Adam(
                d_module[self.curr_stage].parameters(),
                lr=self.train_cfg['lr_d'],
                betas=(0.5, 0.999))

            self.optimizer = dict(
                generator=self.g_optim, discriminator=self.d_optim)

            self.g_scheduler = torch.optim.lr_scheduler.MultiStepLR(
                optimizer=self.g_optim, **self.train_cfg['lr_scheduler_args'])
            self.d_scheduler = torch.optim.lr_scheduler.MultiStepLR(
                optimizer=self.d_optim, **self.train_cfg['lr_scheduler_args'])

        optimizer = self.optimizer

        # setup fixed noises and reals pyramid
        if curr_iter == 0 or len(self.reals) == 0:
            keys = [k for k in data_batch.keys() if 'real_scale' in k]
            scales = len(keys)
            self.reals = [data_batch[f'real_scale{s}'] for s in range(scales)]

            # here we do not padding fixed noises
            self.construct_fixed_noises()

        # disc training
        set_requires_grad(self.discriminator, True)
        for _ in range(self.train_cfg['disc_steps']):
            optimizer['discriminator'].zero_grad()
            # TODO: add noise sampler to customize noise sampling
            with torch.no_grad():
                fake_imgs = self.generator(
                    data_batch['input_sample'],
                    self.fixed_noises,
                    self.noise_weights,
                    rand_mode='rand',
                    curr_scale=self.curr_stage)

            # disc pred for fake imgs and real_imgs
            disc_pred_fake = self.discriminator(fake_imgs.detach(),
                                                self.curr_stage)
            disc_pred_real = self.discriminator(self.reals[self.curr_stage],
                                                self.curr_stage)
            # get data dict to compute losses for disc
            data_dict_ = dict(
                iteration=curr_iter,
                gen=self.generator,
                disc=self.discriminator,
                disc_pred_fake=disc_pred_fake,
                disc_pred_real=disc_pred_real,
                fake_imgs=fake_imgs,
                real_imgs=self.reals[self.curr_stage],
                disc_partial=partial(
                    self.discriminator, curr_scale=self.curr_stage))

            loss_disc, log_vars_disc = self._get_disc_loss(data_dict_)

            # prepare for backward in ddp. If you do not call this function
            # before back propagation, the ddp will not dynamically find the
            # used params in current computation.
            if ddp_reducer is not None:
                ddp_reducer.prepare_for_backward(_find_tensors(loss_disc))
            loss_disc.backward()
            optimizer['discriminator'].step()

        log_vars_disc.update(dict(curr_stage=self.curr_stage))

        # generator training
        set_requires_grad(self.discriminator, False)
        for _ in range(self.train_cfg['generator_steps']):
            optimizer['generator'].zero_grad()

            # TODO: add noise sampler to customize noise sampling
            fake_imgs = self.generator(
                data_batch['input_sample'],
                self.fixed_noises,
                self.noise_weights,
                rand_mode='rand',
                curr_scale=self.curr_stage)
            disc_pred_fake_g = self.discriminator(
                fake_imgs, curr_scale=self.curr_stage)

            recon_imgs = self.generator(
                data_batch['input_sample'],
                self.fixed_noises,
                self.noise_weights,
                rand_mode='recon',
                curr_scale=self.curr_stage)

            data_dict_ = dict(
                iteration=curr_iter,
                gen=self.generator,
                disc=self.discriminator,
                fake_imgs=fake_imgs,
                recon_imgs=recon_imgs,
                real_imgs=self.reals[self.curr_stage],
                disc_pred_fake_g=disc_pred_fake_g)

            loss_gen, log_vars_g = self._get_gen_loss(data_dict_)

            # prepare for backward in ddp. If you do not call this function
            # before back propagation, the ddp will not dynamically find the
            # used params in current computation.
            if ddp_reducer is not None:
                ddp_reducer.prepare_for_backward(_find_tensors(loss_gen))

            loss_gen.backward()
            optimizer['generator'].step()

        # end of each scale
        # calculate noise weight for next scale
        if (curr_iter % self.train_cfg['iters_per_scale']
                == 0) and (self.curr_stage < len(self.reals) - 1):

            with torch.no_grad():
                g_recon = self.generator(
                    data_batch['input_sample'],
                    self.fixed_noises,
                    self.noise_weights,
                    rand_mode='recon',
                    curr_scale=self.curr_stage)
                if isinstance(g_recon, dict):
                    g_recon = g_recon['fake_img']
                g_recon = F.interpolate(
                    g_recon, self.reals[self.curr_stage + 1].shape[-2:])

            mse = F.mse_loss(g_recon.detach(), self.reals[self.curr_stage + 1])
            rmse = torch.sqrt(mse)
            self.noise_weights.append(
                self.train_cfg.get('noise_weight_init', 0.1) * rmse.item())

            # try to release GPU memory.
            torch.cuda.empty_cache()

        log_vars = {}
        log_vars.update(log_vars_g)
        log_vars.update(log_vars_disc)

        results = dict(
            fake_imgs=fake_imgs.cpu(),
            real_imgs=self.reals[self.curr_stage].cpu(),
            recon_imgs=recon_imgs.cpu(),
            curr_stage=self.curr_stage,
            fixed_noises=self.fixed_noises,
            noise_weights=self.noise_weights)
        outputs = dict(log_vars=log_vars, num_samples=1, results=results)

        # update lr scheduler
        self.d_scheduler.step()
        self.g_scheduler.step()

        if hasattr(self, 'iteration'):
            self.iteration += 1

        return outputs


@MODELS.register_module()
class PESinGAN(SinGAN):
    """Positional Encoding in SinGAN.

    This modified SinGAN is used to reimplement the experiments in: Positional
    Encoding as Spatial Inductive Bias in GANs, CVPR2021.
    """

    def _parse_train_cfg(self):
        super(PESinGAN, self)._parse_train_cfg()
        self.fixed_noise_with_pad = self.train_cfg.get('fixed_noise_with_pad',
                                                       False)
        self.first_fixed_noises_ch = self.train_cfg.get(
            'first_fixed_noises_ch', 1)

    def construct_fixed_noises(self):
        """Construct the fixed noises list used in SinGAN."""
        for i, real in enumerate(self.reals):
            h, w = real.shape[-2:]
            if self.fixed_noise_with_pad:
                pad_ = self.get_module(self, 'generator').pad_head
                h += 2 * pad_
                w += 2 * pad_
            if i == 0:
                noise = torch.randn(1, self.first_fixed_noises_ch, h,
                                    w).to(real)
                self.fixed_noises.append(noise)
            else:
                noise = torch.zeros((1, 1, h, w)).to(real)
                self.fixed_noises.append(noise)
