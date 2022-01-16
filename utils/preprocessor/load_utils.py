from models.load import Load
from models.load_type import *
from models.mesh import Mesh
from models.region import Region
import utils.preprocessor.select as sel

def create_load_by_region(id, name, mesh: Mesh, load_type: LoadType, region: Region, value):
    if load_type.target_type == LoadTargetType.NODE:
        load = Load(id, name, load_type, None, None, value)
        load.nodes=sel.select_nodes_by_region(mesh, region)
    elif load_type.target_type == LoadTargetType.ELEMENT:
        load = Load(id, name, load_type, None, None, value)
        load.elems = sel.select_elems_by_region(mesh, region)
    else:
        print('Error: incorrect load destination type')
    return load


