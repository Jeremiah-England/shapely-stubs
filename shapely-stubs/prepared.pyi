from typing import NoReturn

from shapely.geometry.base import BaseGeometry
from shapely.impl import delegated

class PreparedGeometry:
    impl = ...
    def __init__(self, context: BaseGeometry | "PreparedGeometry") -> None: ...
    def __del__(self): ...
    @delegated
    def contains(self, other) -> bool: ...
    @delegated
    def contains_properly(self, other) -> bool: ...
    @delegated
    def covers(self, other) -> bool: ...
    @delegated
    def crosses(self, other) -> bool: ...
    @delegated
    def disjoint(self, other) -> bool: ...
    @delegated
    def intersects(self, other) -> bool: ...
    @delegated
    def overlaps(self, other) -> bool: ...
    @delegated
    def touches(self, other) -> bool: ...
    @delegated
    def within(self, other) -> bool: ...
    def __reduce__(self) -> NoReturn: ...

def prep(ob: BaseGeometry | PreparedGeometry) -> PreparedGeometry: ...
