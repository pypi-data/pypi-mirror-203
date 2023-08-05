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
date     : Mar 13, 2023
email    : Nasy <nasyxx+python@gmail.com>
filename : lorentz.py
project  : jaxrie
license  : GPL-3.0+

Lorentz model.
"""

# Standard Library
from functools import partial

# Types
from jax.typing import ArrayLike

# JAX
import jax
import jax.numpy as jnp

# Local
from .base import BaseManifold

Array = jax.Array


class Lorentz(BaseManifold):
  """Lorentz model."""

  @staticmethod
  @jax.jit
  def add(x: Array, y: Array, k: ArrayLike) -> Array:
    """Addition on manifold with curvature k."""
    pass
