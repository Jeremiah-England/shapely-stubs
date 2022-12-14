from shapely.geometry.base import BaseGeometry

class Validating: ...

class Delegating(Validating):
    def __init__(self, name: str) -> None: ...

class BinaryRealProperty(Delegating):
    def __call__(self, this: BaseGeometry, other: BaseGeometry): ...

class UnaryRealProperty(Delegating):
    def __call__(self, this: BaseGeometry): ...

class BinaryTopologicalOp(Delegating):
    def __call__(self, this: BaseGeometry, other: BaseGeometry, *args): ...

class UnaryTopologicalOp(Delegating):
    def __call__(self, this: BaseGeometry, *args): ...
