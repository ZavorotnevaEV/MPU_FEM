from typing import List
from models.load_type import LoadType
from models.node import Node
from models.element import Element
from models.region import Region

class Load:
    def __init__(self, id, name, type: LoadType, nodes: List[Node]=None, elems: List[Element]=None, value=0):
        self.id = id
        self.name = name
        self.type = type
        self.nodes = nodes
        self.elems = elems
        self.value = value


