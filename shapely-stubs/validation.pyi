from shapely.geometry.base import BaseGeometry

def explain_validity(ob: BaseGeometry) -> str: ...
def make_valid(ob: BaseGeometry) -> BaseException: ...
