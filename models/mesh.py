from typing import List

from models.element import Element
from models.node import Node


class Mesh:
    def __init__(self, nodes: List[Node], elements: List[Element]):
        self.nodes = nodes
        self.elements = elements
