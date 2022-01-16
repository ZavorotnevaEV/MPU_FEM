import select as sel
from models.material import Material
from models.region import Region
from models.mesh import Mesh

def apply_material(material: Material, region: Region, mesh: Mesh) -> None:
    elems = sel.select_elems_by_region(region, mesh)
    for elem in elems:
        elem.material = material
