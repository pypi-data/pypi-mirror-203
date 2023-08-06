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
date     : Apr 12, 2023
email    : Nasy <nasyxx+python@gmail.com>
filename : euclidean.py
project  : jaxrie
license  : GPL-3.0+

This is the module for the Euclidean manifold.
"""
# Standard Library
from functools import partial

# Types
from jax.typing import ArrayLike

# JAX
import jax

# Local
from ._base import EPS, BaseManifold

Array = jax.Array


class Euclidean(BaseManifold):
  """The universal Stereographic projection model."""

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def add(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius addition on manifold with curvature k."""
    del k, eps
    return x + y

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def adde(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius addition on manifold (left H, right E) with curvature k."""
    return Euclidean.add(x, y, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def sub(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius subtraction on manifold with curvature k."""
    return Euclidean.add(x, -y, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def mul(r: Array, x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius multiplication on manifold with curvature k."""
    del k, eps
    return r * x

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matvec(m: Array, x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius matrix vector multiplication on manifold with curvature k."""
    del k, eps
    return m @ x

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matmul(x1: Array, x2: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Mobius matrix multiplication on manifold with curvature k."""
    del k, eps
    return x1 @ x2

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matmull(x1: Array, x2: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Matrix multiplication (left H, right E) with curvature k."""
    return Euclidean.matmul(x1, x2, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def matmulr(x1: Array, x2: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Matrix multiplication (left E, right H) with curvature k."""
    return Euclidean.matmul(x1, x2, k, eps)

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def expmap(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Exponential map on manifold with curvature k."""
    del k, eps
    return x + y

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def logmap(x: Array, y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Logarithm map on manifold with curvature k."""
    del k, eps
    return y - x

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def expmap0(u: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Exponential map on manifold with curvature k."""
    del k, eps
    return u

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def logmap0(y: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Logarithm map on manifold with curvature k."""
    del k, eps
    return y

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def egrad2rgrad(x: Array, grad: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Euclidean gradient to Riemannian gradient."""
    del x, k, eps
    return grad

  @staticmethod
  @partial(jax.jit, static_argnames=("eps",))
  def proj(x: Array, k: ArrayLike, eps: float = EPS) -> Array:
    """Projection on manifold with curvature k."""
    del k, eps
    return x
