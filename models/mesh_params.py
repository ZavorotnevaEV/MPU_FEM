from models.mesh_type import MeshType
from models.material import Material
from models.property import Property
from models.element_type import *

class MeshParams:
    def __init__(self, id, geometry, pid: Property, element_type: ElementType, mat: Material, divisions, mesh_type: MeshType):
        self.id = id
        self.geometry = geometry
        self.pid = pid
        self.task_type = element_type
        self.material = mat
        self.divisions = divisions
        self.mesh_type = mesh_type