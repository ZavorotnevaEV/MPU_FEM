from models.mesh import Mesh
from models.region import Region
from models.region_type import RegionType
import numpy as np


def select_nodes_by_region(mesh: Mesh, region: Region):
    sel_nodes = []
    if region.type == RegionType.POINT:
        for node in mesh.nodes:
            if node.coord_x == region.params[0] and (
                    node.coord_y == region.params[1]):
                sel_nodes.append(node)
    if region.type == RegionType.LINE_X:
        for node in mesh.nodes:
            if node.coord_x == region.params[0]:
                sel_nodes.append(node)
    elif region.type == RegionType.LINE_Y:
        for node in mesh.nodes:
            if node.coord_y == region.params[0]:
                sel_nodes.append(node)
    elif region.type == RegionType.RECTANGLE:
        for node in mesh.nodes:
            if (node.coord_x >= region.params[0]) and (
                    (node.coord_y >= region.params[2])) and (
                    (node.coord_x <= region.params[1])) and (
                    (node.coord_y <= region.params[3])):
                sel_nodes.append(node)
    else:
        print('Error: incorrect region type')

    return sel_nodes


def select_elems_by_region(mesh: Mesh,region: Region):
    sel_elems=[]
    if region.type == RegionType.RECTANGLE:
         for element in mesh.elements:
             if region.params[0] < element.center_x < region.params[1] and region.params[2] < element.center_y< region.params[3]:
                 sel_elems.append(element)
    return sel_elems
