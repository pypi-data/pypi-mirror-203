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
filename : stereographic.py
project  : jaxrie
license  : GPL-3.0+

This is the universal model in stereographic projection.

Include Hyperbolic (Poincare) k < 0, Euclidean k = 0, and Spherical k > 0.
"""

# Standard Library
from functools import partial

# Types
from jax.typing import ArrayLike

# JAX
import jax

# Local
from ._base import BaseManifold
from ._math import (EPS, mobius_add, mobius_adde, mobius_matmulh,
                    mobius_matmull, mobius_matmulr, mobius_matvec_mul,
                    mobius_scala_mul, stereo_egrad2rgrad, stereo_expmap,
                    stereo_expmap0, stereo_logmap, stereo_logmap0, stereo_proj,
                    stereo_ptrans, tangent_inner, tangent_norm, tangent_sqnorm)

Array = jax.Array


class Stereographic(BaseManifold):
  """The universal Stereographic projection model."""

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def add(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius addition on manifold with curvature k."""
    return mobius_add(x, y, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def adde(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius addition on manifold (left H, right E) with curvature k."""
    return mobius_adde(x, y, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def sub(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius subtraction on manifold with curvature k."""
    return mobius_add(x, -y, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def mul(r: Array, x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius multiplication on manifold with curvature k."""
    return mobius_scala_mul(r, x, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matvec(m: Array, x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius matrix vector multiplication on manifold with curvature k."""
    return mobius_matvec_mul(m, x, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matmul(x1: Array, x2: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius matrix multiplication on manifold with curvature k."""
    return mobius_matmulh(x1, x2, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matmull(x1: Array, x2: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Matrix multiplication (left H, right E) with curvature k."""
    return mobius_matmull(x1, x2, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matmulr(x1: Array, x2: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Matrix multiplication (left E, right H) with curvature k."""
    return mobius_matmulr(x1, x2, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def expmap(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Exponential map on manifold with curvature k."""
    return stereo_expmap(x, y, k, axis=-1, eps=eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def logmap(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Logarithm map on manifold with curvature k."""
    return stereo_logmap(x, y, k, axis=-1, eps=eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def expmap0(u: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Exponential map on manifold with curvature k."""
    return stereo_expmap0(u, k, axis=-1, eps=eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def logmap0(y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Logarithm map on manifold with curvature k."""
    return stereo_logmap0(y, k, axis=-1, eps=eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def egrad2rgrad(x: Array, grad: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Euclidean gradient to Riemannian gradient."""
    return stereo_egrad2rgrad(x, grad, k, eps=eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def proj(x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Projection on manifold with curvature k."""
    return stereo_proj(x, k, eps=eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def norm(x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Norm on manifold with curvature k."""
    return tangent_norm(x, k, eps=eps, axis=-1, keepdims=True)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def sqnorm(x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Squared norm on manifold with curvature k."""
    return tangent_sqnorm(x, k, eps=eps, axis=-1, keepdims=True)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def inner(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Inner product on manifold with curvature k."""
    return tangent_inner(x, y, k, eps=eps, axis=-1, keepdims=True)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def ptransp(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Parallel transport on manifold with curvature k."""
    return stereo_ptrans(x, y, k, eps=eps)
