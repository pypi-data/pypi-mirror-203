import jax
import jax.lax as lax
import jax.numpy as jnp

import flax
import flax.linen as nn

import numpy as np
import einops

from functools import partial
from typing import Sequence, Literal, Optional

from FlaxSR.layers import DropPath


def _window_partition(inputs: jnp.ndarray, window_size: int) -> jnp.ndarray:
    return einops.rearrange(inputs, 'B (H H_W) (W W_W) C -> (B H W) H_W W_W C', H_W=window_size, W_W=window_size)


def _window_reverse(inputs: jnp.ndarray, h: int, w: int) -> jnp.ndarray:
    return einops.rearrange(inputs, '(B H W) H_W W_W C -> B (H H_W) (W W_W) C', H=h, W=w)
