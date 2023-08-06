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
date     : Apr  7, 2023
email    : Nasy <nasyxx+python@gmail.com>
filename : basic.py
project  : jaxrie
license  : GPL-3.0+

Basic
"""

# Standard Library
from collections.abc import Callable
from dataclasses import dataclass

# Types
from jax.typing import ArrayLike

# JAX
import haiku as hk
import jax
import jax.numpy as jnp

# Local
from jaxrie.manifold import Manifold

Array = jax.Array


def init_wrap(
    manifold: Manifold, k: ArrayLike, init: hk.initializers.Initializer
) -> hk.initializers.Initializer:
  """Wrap the initializer."""
  return lambda shape, dtype: manifold.expmap0(init(shape, dtype), k)


@dataclass
class HAct(hk.Module):
  """Hyperbolic Activation Layer."""

  activation: Callable[[Array], Array]
  manifold: Manifold
  kin: ArrayLike
  kout: ArrayLike

  def __call__(self, x: Array) -> Array:
    """Apply the layer."""
    dtype = x.dtype
    m = self.manifold
    self.kin = jnp.array(self.kin, dtype=dtype)
    self.kout = jnp.array(self.kout, dtype=dtype)

    return m.proj(
        m.expmap0(self.activation(m.logmap0(x, self.kin)), self.kout),
        self.kout,
    )


class HLinear(hk.Module):
  """Hyperbolic Linear Layer."""

  def __init__(
      self,
      out_features: int,
      manifold: Manifold,
      k: ArrayLike | None = None,
      with_bias: bool = True,
      w_init: hk.initializers.Initializer | None = None,
      b_init: hk.initializers.Initializer | None = None,
      name: str | None = None,
  ) -> None:
    """Initialize the layer."""
    super().__init__(name=name)
    self.out_features = out_features
    self.m = manifold

    self.tk = k is None
    self.k = -1.0 if k is None else k
    self.w_init = w_init
    self.b_init = b_init or hk.initializers.Constant(0.0)
    self.with_bias = with_bias

  def __call__(self, x: Array) -> Array:
    """Apply the layer."""
    dtype = x.dtype
    input_size = self.input_size = x.shape[-1]
    w_init = self.w_init

    self.k = jnp.array(self.k, dtype=dtype)
    if self.tk:
      self.k = hk.get_parameter("rie_k", (), init=hk.initializers.Constant(self.k))

    if w_init is None:
      stddev = 1.0 / jnp.sqrt(input_size)
      w_init = init_wrap(self.m, self.k, hk.initializers.TruncatedNormal(stddev=stddev))
    w = hk.get_parameter("rie_w", [input_size, self.out_features], dtype, init=w_init)

    out = self.m.proj(self.m.matmul(x, w, self.k), self.k)

    if self.with_bias:
      b = hk.get_parameter("rie_b", [self.out_features], dtype, init=self.b_init)
      out = self.m.proj(self.m.add(out, b, self.k), self.k)

    hk.set_state("k", self.k)
    return out


class HGCN(hk.Module):
  """Hyperbolic Graph Convolutional Network."""

  def __init__(
      self,
      out_features: int,
      manifold: Manifold,
      k: ArrayLike | None = None,
      with_bias: bool = True,
      w_init: hk.initializers.Initializer | None = None,
      b_init: hk.initializers.Initializer | None = None,
      name: str | None = None,
  ) -> None:
    """Initialize the layer."""
    super().__init__(name=name)
    self.out_features = out_features
    self.m = manifold
    self.with_bias = with_bias

    w_init = w_init or hk.initializers.VarianceScaling(1.0, "fan_avg", "uniform")

    self.linear = HLinear(
        out_features,
        manifold,
        k=k,
        with_bias=with_bias,
        w_init=w_init,
        b_init=b_init,
        name="project",
    )

  def __call__(self, x: Array, adj: Array) -> Array:
    """Apply the layer."""
    out = self.linear(x)
    self.k = self.linear.k
    hk.set_state("k", self.k)
    return self.m.proj(self.m.matmulr(adj, out, self.k), self.k)
