from enum import Enum
from typing import List
from models.material_property import MaterialProperty

class MaterialType(Enum):
    THERMAL_ISOTROPIC = (1, [1, 2, 3])

    def __init__(self, id, mat_props_ids: List[int]):
        self.id = id
        self.mat_props = mat_props_ids



