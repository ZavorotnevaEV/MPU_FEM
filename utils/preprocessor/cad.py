from models.geometry import Geometry
from models.geometry_type import GeometryType

def create_rectangle(id, name, x1, y1, x2, y2):
    return Geometry(id, name, GeometryType.RECTANGLE, [x1, y1, x2, y2])