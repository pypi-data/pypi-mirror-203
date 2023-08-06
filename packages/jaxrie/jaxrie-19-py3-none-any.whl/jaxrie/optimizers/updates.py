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
filename : updates.py
project  : jaxrie
license  : GPL-3.0+

Updates
"""
# Types
from jax.typing import ArrayLike

# JAX
import haiku as hk
import jax
import jax.numpy as jnp
import optax

# Local
from jaxrie import Manifold

Array = jax.Array
DK = jax.tree_util.DictKey


def get_k(
    states: hk.State,
    ks: tuple[DK, DK],
    idx: int = 0,
    key: str = "rie_k",
    k: ArrayLike = -1.0,
) -> Array:
  """Get the curvature."""
  k = jnp.asarray(k)
  return states.get(str(ks[idx].key), {key: k})[key]


def apply_riemannian_updates(
    params: hk.Params,
    updates: optax.Updates,
    states: hk.State,
    manifold: Manifold,
    k: ArrayLike = -1.0,
) -> hk.Params:
  """Apply the riemannian update to the corresponding parameters."""

  def aru_helper(ks: tuple[DK, DK], param: Array, update: Array) -> Array:
    """Apply the helper function for rie updates."""
    dtype = jnp.asarray(param).dtype
    shape = jnp.asarray(param).shape
    return jnp.asarray(
        manifold.expmap(param, update, get_k(states, ks, k=k))
        .astype(dtype)
        .reshape(shape)
    )

  return jax.tree_util.tree_map_with_path(
      aru_helper,
      params,
      updates,
  )


def apply_mix_updates(
    params: hk.Params,
    updates: optax.Updates,
    states: hk.State,
    manifold: Manifold,
    k: ArrayLike = -1.0,
) -> hk.Params:
  """Apply the mix update to the corresponding parameters."""

  def update_fn(ks: tuple[DK, DK], param: Array, update: Array) -> Array:
    """Update the params by the updates."""
    dtype = jnp.asarray(param).dtype
    if str(ks[1].key).startswith("rie_"):
      k_in = get_k(states, ks, k=k)
      return (
          manifold.proj(
              manifold.expmap(param, update, k_in),
              k_in,
          )
          .astype(dtype)
          .squeeze()
      )
    return jnp.asarray(param + update, dtype=dtype)

  return jax.tree_util.tree_map_with_path(
      update_fn,
      params,
      updates,
  )
