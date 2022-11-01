from collections.abc import Sequence
from typing import Literal, TypeAlias, TypeVar

from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry

_BaseGeometryTypeVar = TypeVar("_BaseGeometryTypeVar", bound=BaseGeometry)
_OriginKeywords = Literal["center", "centroid"]
_Origin: TypeAlias = _OriginKeywords | Point | Sequence[float]

def affine_transform(
    geom: _BaseGeometryTypeVar, matrix: Sequence[float]
) -> _BaseGeometryTypeVar: ...
def interpret_origin(
    geom: BaseGeometry, origin: _Origin, ndim: Literal[2, 3]
) -> Sequence[float]: ...
def rotate(
    geom: _BaseGeometryTypeVar,
    angle: float,
    origin: _Origin = ...,
    use_radians: bool = ...,
) -> _BaseGeometryTypeVar: ...
def scale(
    geom: _BaseGeometryTypeVar,
    xfact: float = ...,
    yfact: float = ...,
    zfact: float = ...,
    origin: _Origin = ...,
) -> _BaseGeometryTypeVar: ...
def skew(
    geom: _BaseGeometryTypeVar,
    xs: float = ...,
    ys: float = ...,
    origin: _Origin = ...,
    use_radians: bool = ...,
) -> _BaseGeometryTypeVar: ...
def translate(
    geom: _BaseGeometryTypeVar, xoff: float = ..., yoff: float = ..., zoff: float = ...
) -> _BaseGeometryTypeVar: ...
