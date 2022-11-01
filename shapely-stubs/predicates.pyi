from shapely.topology import Delegating

class BinaryPredicate(Delegating):
    def __call__(self, this, other, *args): ...

class UnaryPredicate(Delegating):
    def __call__(self, this): ...
