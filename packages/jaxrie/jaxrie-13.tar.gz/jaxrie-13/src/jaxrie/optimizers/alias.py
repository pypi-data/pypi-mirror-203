#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""Python ♡ Nasy.

    |             *         *
    |                  .                .
    |           .                              登
    |     *                      ,
    |                   .                      至
    |
    |                               *          恖
    |          |\___/|
    |          )    -(             .           聖 ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Apr 16, 2023
email    : Nasy <nasyxx+python@gmail.com>
filename : alias.py
project  : jaxrie
license  : GPL-3.0+

Alias.
"""


# Types
from typing import Any

# JAX
import optax

# Local
from . import transform
from jaxrie import Manifold

ScalarOrSchedule = float | optax.Schedule


def _scale_by_learning_rate(
    learning_rate: ScalarOrSchedule, flip_sign: bool = True
) -> optax.GradientTransformation:
  """Update by learning rate."""
  m = -1 if flip_sign else 1
  if callable(learning_rate):
    return optax.scale_by_schedule(lambda count: m * learning_rate(count))  # type: ignore[operator]  # noqa: E501
  return optax.scale(m * learning_rate)


def riemannian_sgd(
    manifold: Manifold,
    learning_rate: ScalarOrSchedule,
) -> optax.GradientTransformation:
  """Run Riemannian Stochastic Gradient Descent optimizer."""
  return optax.chain(
      transform.riemannian_scale(manifold),
      _scale_by_learning_rate(learning_rate),
  )


def riemannian_adam(
    manifold: Manifold,
    learning_rate: ScalarOrSchedule,
    b1: float = 0.9,
    b2: float = 0.999,
    eps: float = 1e-8,
    eps_root: float = 1e-8,
    mu_dtype: Any | None = None,
) -> optax.GradientTransformation:
  """Run the Riemannian Adam optimizer."""
  return optax.chain(
      transform.riemannian_scale(manifold),
      transform.scale_rie_by_adam(
          manifold=manifold,
          b1=b1,
          b2=b2,
          eps=eps,
          eps_root=eps_root,
          mu_dtype=mu_dtype,
      ),
      _scale_by_learning_rate(learning_rate),
  )


def riemannian_adamw(
    manifold: Manifold,
    learning_rate: ScalarOrSchedule,
    b1: float = 0.9,
    b2: float = 0.999,
    eps: float = 1e-8,
    eps_root: float = 0.0,
    mu_dtype: Any | None = None,
    weight_decay: float = 1e-4,
    mask: Any | None = None,
) -> optax.GradientTransformation:
  """Run the Riemannian AdamW optimizer."""
  return optax.chain(
      transform.riemannian_scale(manifold),
      transform.scale_rie_by_adam(
          manifold=manifold,
          b1=b1,
          b2=b2,
          eps=eps,
          eps_root=eps_root,
          mu_dtype=mu_dtype,
      ),
      optax.add_decayed_weights(weight_decay, mask),
      _scale_by_learning_rate(learning_rate),
  )


def rsgd(
    manifold: Manifold,
    elr: ScalarOrSchedule,
    rlr: ScalarOrSchedule,
) -> optax.GradientTransformation:
  """Run Riemannian Stochastic Gradient Descent optimizer."""
  return transform.mix_opt(
      optax.sgd(elr),
      riemannian_sgd(manifold, rlr),
  )


def rie_adam(
    manifold: Manifold,
    elr: ScalarOrSchedule,
    rlr: ScalarOrSchedule,
    b1: float = 0.9,
    b2: float = 0.999,
) -> optax.GradientTransformation:
  """Run the Riemannian Adam optimizer."""
  return transform.mix_opt(
      optax.adam(elr, b1, b2),
      riemannian_adam(manifold, rlr, b1, b2),
  )


def rie_adamw(
    manifold: Manifold,
    elr: ScalarOrSchedule,
    rlr: ScalarOrSchedule,
    b1: float = 0.9,
    b2: float = 0.999,
    weight_decay: float = 1e-4,
    mask: Any | None = None,
) -> optax.GradientTransformation:
  """Run the Riemannian AdamW optimizer."""
  return transform.mix_opt(
      optax.adamw(elr, b1, b2, weight_decay=weight_decay, mask=mask),
      riemannian_adamw(manifold, rlr, b1, b2, weight_decay=weight_decay, mask=mask),
  )
