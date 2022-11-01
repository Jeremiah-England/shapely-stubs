from typing import TypeAlias

from shapely.geometry import LinearRing, LineString, MultiLineString
from shapely.geometry.base import BaseGeometry
from shapely.topology import Delegating

_LinearGeometry: TypeAlias = LineString | LinearRing | MultiLineString

class LinearRefBase(Delegating): ...

class ProjectOp(LinearRefBase):
    def __call__(self, this: _LinearGeometry, other: BaseGeometry): ...

class InterpolateOp(LinearRefBase):
    def __call__(self, this: _LinearGeometry, distance: float): ...
