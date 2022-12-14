from typing import Callable, Sequence, TypeVar, Union

from shapely.geometry import GeometryCollection, LineString, MultiLineString, Point
from shapely.geometry.base import BaseGeometry
from typing_extensions import Any

_BaseGeometryTypeVar = TypeVar("_BaseGeometryTypeVar", bound=BaseGeometry)

class CollectionOperator:
    def shapeup(self, ob): ...
    def polygonize(self, lines): ...
    def polygonize_full(self, lines): ...
    def linemerge(self, lines) -> MultiLineString | LineString | GeometryCollection: ...
    def cascaded_union(self, geoms) -> BaseGeometry: ...
    def unary_union(self, geoms) -> BaseGeometry: ...

operator: CollectionOperator = ...
polygonize: Callable[[Any], Any] = ...
polygonize_full: Callable[[Any], Any] = ...
linemerge: Callable[[Any], MultiLineString | LineString | GeometryCollection] = ...
cascaded_union: Callable[[Any], BaseGeometry] = ...
unary_union: Callable[[Any], BaseGeometry] = ...

def triangulate(
    geom: BaseGeometry, tolerance: float = ..., edges: bool = ...
) -> list[BaseGeometry]: ...
def voronoi_diagram(
    geom: BaseGeometry,
    envelop: BaseGeometry | None = ...,
    tolerance: float = ...,
    edges: bool = ...,
) -> GeometryCollection: ...

validate: Callable[[Any], Any] = ...

def transform(
    func: Union[
        Callable[[float, float, float | None], Sequence[float | None]],
        Callable[[float, float], Sequence[float]],
        Callable[
            [Sequence[float], Sequence[float], Sequence[float | None] | None],
            Sequence[Sequence[float]],
        ],
        Callable[[Sequence[float], Sequence[float]], Sequence[Sequence[float]]],
    ],
    geom: _BaseGeometryTypeVar,
) -> _BaseGeometryTypeVar: ...
def nearest_points(g1: BaseGeometry, g2: BaseGeometry) -> tuple[Point, Point]: ...
def snap(
    g1: _BaseGeometryTypeVar, g2: BaseGeometry, tolerance: float
) -> _BaseGeometryTypeVar: ...
def shared_paths(g1: LineString, g2: LineString) -> GeometryCollection: ...

split: Callable[[BaseGeometry, BaseGeometry], GeometryCollection] = ...

def substring(
    geom: LineString, start_dist: float, end_dist: float, normalized: bool = ...
) -> Point | LineString: ...
def clip_by_rect(
    geom: BaseGeometry, xmin: float, ymin: float, xmax: float, ymax: float
) -> BaseGeometry: ...
def orient(geom: _BaseGeometryTypeVar, sign: float = ...) -> _BaseGeometryTypeVar: ...
