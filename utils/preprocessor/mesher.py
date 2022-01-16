from models.element import Element
from models.geometry_type import GeometryType
from models.geometry import Geometry
from models.node import Node
from models.mesh import Mesh
from models.mesh_params import MeshParams
from models.element_type import *
from models.fe_model import FeModel

def rect_mesh(mesh_param: MeshParams):
        if mesh_param.geometry.type == GeometryType.RECTANGLE:
            x1 = mesh_param.geometry.dimensions[0]
            x2 = mesh_param.geometry.dimensions[1]
            y1 = mesh_param.geometry.dimensions[2]
            y2 = mesh_param.geometry.dimensions[3]
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            nx = mesh_param.divisions[0]
            ny = mesh_param.divisions[1]
            sx = dx / nx
            sy = dy / ny
            nodes = []
            idnod = 1
            for yy in range(ny + 1):
                for xx in range(nx + 1):
                    nodes.append(Node(idnod, xx * sx + x1, yy * sy + y1))
                    idnod += 1
            elements = []
            idelem = 1
            for firstNode in nodes:
                if firstNode.coord_x != x2 and firstNode.coord_y != y2:
                    n1 = firstNode
                    n2 = nodes[n1.id]
                    n3 = nodes[n1.id + nx + 1]
                    n4 = nodes[n1.id + nx]
                    elements.append(Element(idelem, mesh_param.pid, ElementType.T2Q4, [n1, n2, n3, n4], mesh_param.material))
            mesh1 = Mesh(nodes, elements)
            return mesh1
        else:
            print('Error: unsupported geometry type')
