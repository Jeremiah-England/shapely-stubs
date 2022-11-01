from shapely.geometry.base import BaseGeometry
from shapely.topology import Delegating

class BinaryPredicate(Delegating):
    def __call__(self, this: BaseGeometry, other: BaseGeometry, *args): ...

class UnaryPredicate(Delegating):
    def __call__(self, this: BaseGeometry): ...
