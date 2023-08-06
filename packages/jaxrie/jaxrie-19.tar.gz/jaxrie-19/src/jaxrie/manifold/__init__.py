# Local
from . import _math as math
from ._base import BaseManifold as Manifold
from ._euclidean import Euclidean
from ._stereographic import Stereographic

euclidean = Euclidean()
stereographic = Stereographic()


__all__ = [
    "Manifold",
    "Euclidean",
    "euclidean",
    "Stereographic",
    "stereographic",
    "math",
]
