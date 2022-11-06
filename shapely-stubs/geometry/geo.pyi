from typing import Literal, Protocol, TypeAlias, TypedDict

from shapely.geometry.base import BaseGeometry
from shapely.geometry.collection import GeometryCollection
from shapely.geometry.polygon import Polygon
from shapely.geometry.proxy import CachingGeometryProxy

class _GeoInterfaceBase(TypedDict):
    type: str
    coordinates: tuple

class _GeoInterfaceCollection(TypedDict):
    type: Literal["GeometryCollection"]
    geometries: list[_GeoInterfaceBase]

class _GeoInterfaceCollectionEmpty(TypedDict):
    type: Literal["GeometryCollection"]

_GeoInterface: TypeAlias = (
    _GeoInterfaceBase | _GeoInterfaceCollection | _GeoInterfaceCollectionEmpty
)

class _HasGeoInterface(Protocol):
    __geo_interface__: _GeoInterface

def box(
    minx: float, miny: float, maxx: float, maxy: float, ccw: bool = ...
) -> Polygon: ...
def shape(
    context: _GeoInterface,
) -> BaseGeometry: ...
def asShape(
    context: _GeoInterface,
) -> CachingGeometryProxy | GeometryCollection: ...
def mapping(ob: _HasGeoInterface) -> _GeoInterface: ...
