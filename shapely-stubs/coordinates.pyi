from collections.abc import Callable, Sequence
from typing import TypeAlias, TypeVar, overload

import numpy as np
import numpy.typing as npt
from shapely.lib import Geometry

# A reasonable placeholder till I figure out the exact type of this thing!
_GeometryArrayLike: TypeAlias = Sequence[Geometry] | npt.NDArray[np.object_]
_GeometryTypeVar = TypeVar("_GeometryTypeVar", bound=Geometry)
_TransformFunction: TypeAlias = Callable[
    [npt.NDArray[np.float64]], npt.NDArray[np.float64]
]

@overload
def transform(
    geometry: _GeometryTypeVar,
    transformation: _TransformFunction,
    include_z: bool = ...,
) -> _GeometryTypeVar: ...
@overload
def transform(
    geometry: _GeometryArrayLike,
    transformation: _TransformFunction,
    include_z: bool = ...,
) -> npt.NDArray[np.object_]: ...
@overload
def transform(
    geometry: Geometry | _GeometryArrayLike,
    transformation: _TransformFunction,
    include_z: bool = ...,
) -> Geometry | npt.NDArray[np.object_]: ...
def transform(
    geometry: Geometry | _GeometryArrayLike,
    transformation: _TransformFunction,
    include_z: bool = ...,
) -> Geometry | npt.NDArray[np.object_]: ...
def count_coordinates(geometry): ...
def get_coordinates(geometry, include_z: bool = ..., return_index: bool = ...): ...
def set_coordinates(geometry, coordinates): ...
