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
# JAX
import haiku as hk
import jax
import jax.numpy as jnp
import optax

# Local
from jaxrie import Manifold

Array = jax.Array
DK = jax.tree_util.DictKey


def apply_riemannian_updates(
    params: hk.Params, updates: optax.Updates, manifold: Manifold
) -> optax.Params:
  """Apply the riemannian update to the corresponding parameters."""
  return jax.tree_util.tree_map_with_path(
      lambda mn, _, p, u: jnp.asarray(
          manifold.expmap(p, u, params[mn]["rie_k"]).astype(jnp.asarray(p).dtype)
      ),
      params,
      updates,
  )


def apply_mix_updates(
    params: hk.Params, updates: optax.Updates, manifold: Manifold
) -> optax.Params:
  """Apply the mix update to the corresponding parameters."""

  def _label_fn(params: hk.Params) -> dict[str, dict[str, str]]:
    """Generate labels by function for params."""
    return jax.tree_util.tree_map_with_path(
        lambda ks, _: "rie" if ks[1].key.startswith("rie") else "euc", params
    )

  def update_fn(ks: tuple[DK, DK], param: Array, update: Array, label: str) -> Array:
    """Update the params by the updates."""
    dtype = jnp.asarray(param).dtype
    if label == "rie":
      k = params[str(ks[0].key)]["rie_k"]
      return manifold.proj(
          manifold.expmap(param, update, k),
          k,
      ).astype(dtype)
    return jnp.asarray(param + update, dtype=dtype)

  return jax.tree_util.tree_map_with_path(
      update_fn,
      params,
      updates,
      _label_fn(params),
  )
