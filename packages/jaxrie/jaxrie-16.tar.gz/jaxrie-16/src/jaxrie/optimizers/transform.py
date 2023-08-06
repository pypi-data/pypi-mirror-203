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
filename : transform.py
project  : jaxrie
license  : GPL-3.0+

Transform of the data.


For haiku parameters like only.
  TODO: Find a better way to get the curvature.
"""
# Standard Library
from functools import partial

# Types
from typing import Any, NamedTuple, cast

# JAX
import haiku as hk
import jax
import jax.numpy as jnp
import optax
from optax import bias_correction, update_moment  # type: ignore[attr-defined]
from optax._src.utils import canonicalize_dtype, cast_tree

# Local
from .updates import apply_riemannian_updates, get_k
from jaxrie import Manifold

Array = jax.Array


def mix_opt(
    euc: optax.GradientTransformation, rie: optax.GradientTransformation
) -> optax.GradientTransformationExtraArgs:
  """Mix euclidean and riemannian optimizer."""
  euc_mask = partial(
      hk.data_structures.map, lambda _, name, _v: not name.startswith("rie_")
  )
  rie_mask = partial(
      hk.data_structures.map, lambda _, name, _v: name.startswith("rie_")
  )
  return optax.chain(
      optax.masked(euc, euc_mask),
      optax.masked(rie, rie_mask),
  )


def riemannian_scale(manifold: Manifold) -> optax.GradientTransformationExtraArgs:
  """Riemannian scale."""

  def init_fn(params: optax.Params) -> optax.OptState:
    del params
    return optax.ScaleState()

  def update_fn(
      grads: hk.Params,
      state: optax.OptState,
      params: hk.Params,
      states: hk.State,
      eps: float = 4e-3,
  ) -> tuple[hk.Params, optax.OptState]:
    """Update the scale."""
    return (
        jax.tree_util.tree_map_with_path(
            lambda ks, g, p: manifold.egrad2rgrad(p, g, get_k(states, ks), eps=eps),
            grads,
            params,
        ),
        state,
    )

  return optax.GradientTransformationExtraArgs(init_fn, update_fn)  # type: ignore[arg-type]  # noqa: E501


class RieAdamState(NamedTuple):
  """Riemannian Adam state."""

  count_: Array  # for mypy bug #3950: tuple has a method named count
  mu: optax.Updates
  nu: optax.Updates
  tau: optax.Updates


def scale_rie_by_adam(
    manifold: Manifold,
    b1: float = 0.9,
    b2: float = 0.999,
    eps: float = 1e-8,
    eps_root: float = 0.0,
    mu_dtype: Any | None = None,
) -> optax.GradientTransformationExtraArgs:
  """Riemannian scale by Adam."""
  mu_dtype = canonicalize_dtype(mu_dtype)

  def init_fn(params: optax.Params) -> RieAdamState:
    return RieAdamState(
        count_=jnp.zeros((), dtype=jnp.int32),
        mu=jax.tree_util.tree_map(lambda x: jnp.zeros_like(x, dtype=mu_dtype), params),
        nu=jax.tree_util.tree_map(lambda x: jnp.zeros_like(x, dtype=mu_dtype), params),
        tau=jax.tree_util.tree_map(lambda x: jnp.zeros_like(x, dtype=mu_dtype), params),
    )

  def update_fn(
      grads: hk.Params,
      state: RieAdamState,
      params: hk.Params,
      states: hk.State,
  ) -> tuple[hk.Params, RieAdamState]:
    """Update the scale."""
    count_inc = cast(Array, optax.safe_int32_increment(state.count_))

    mu = update_moment(grads, state.tau, b1, 1)

    sqnorm_grads = jax.tree_util.tree_map_with_path(
        lambda ks, g: manifold.sqnorm(g, get_k(states, ks)), grads
    )
    nu = update_moment(sqnorm_grads, state.nu, b2, 1)

    muhat = bias_correction(mu, b1, count_inc)
    nuhat = bias_correction(nu, b2, count_inc)

    updates = jax.tree_util.tree_map(
        lambda m, n: m / (jnp.sqrt(n + eps_root) + eps), muhat, nuhat
    )
    mu = cast_tree(mu, mu_dtype)

    new_params = apply_riemannian_updates(params, updates, states, manifold)

    tau = jax.tree_util.tree_map_with_path(
        lambda ks, p, np, m: manifold.ptransp(p, np, m, get_k(states, ks)),
        params,
        new_params,
        mu,
    )

    return updates, RieAdamState(count_inc, mu, nu, tau)

  return optax.GradientTransformationExtraArgs(init_fn, update_fn)  # type: ignore[arg-type]  # noqa: E501
