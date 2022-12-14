from typing import Generator, Iterable

from shapely.geometry.base import BaseGeometry
from shapely.topology import Delegating

class IterOp(Delegating):
    def __call__(
        self, context: BaseGeometry, iterator: Iterable[BaseGeometry], value: bool = ...
    ) -> Generator[BaseGeometry, None, None]: ...

disjoint: IterOp = ...
touches: IterOp = ...
intersects: IterOp = ...
crosses: IterOp = ...
within: IterOp = ...
contains: IterOp = ...
overlaps: IterOp = ...
equals: IterOp = ...
