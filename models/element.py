from typing import List

from models.element_type import ElementType
from models.node import Node
from models.property import Property
from models.material import Material

class Element:

    def __init__(self, id: int, pid: Property, type: ElementType, nodes: List[Node], material: Material=None):
        self.id = id
        self.pid = id
        self.type = type
        self.material = material
        self.nodes = nodes
        self.__calculate_center()
        self.__calculate_volume()
        self.__calculate_jacobian()


    def __calculate_center(self)->None:
        self.center_x = sum([node.coord_x for node in self.nodes]) / len(self.nodes)
        self.center_y = sum([node.coord_y for node in self.nodes]) / len(self.nodes)

    def __calculate_volume(self)->None:
        pass

    def __calculate_jacobian(self)->None:
        pass




