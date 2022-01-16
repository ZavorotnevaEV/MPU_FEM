from enum import Enum

class LoadTargetType(Enum):
    NODE = 1
    ELEMENT = 2

class LoadClass(Enum):
    DIRICHLET = 1
    NEUMANN = 2
    NEWTON = 3
    VOLUME = 4

class LoadType(Enum):
    TEMP = (1, LoadClass.DIRICHLET, LoadTargetType.NODE)
    THERMAL_FLUX = (2, LoadClass.NEUMANN, LoadTargetType.NODE)
    HEATGEN = (3, LoadClass.VOLUME, LoadTargetType.ELEMENT)
    DISPLACEMENT = (4, LoadClass.DIRICHLET, LoadTargetType.NODE)
    FORCE = (5, LoadClass.NEUMANN, LoadTargetType.NODE)
    MOMENT = (6, LoadClass.NEUMANN, LoadTargetType.NODE)
    
    def __init__(self, id, load_class: LoadClass, target: LoadTargetType):
        self.id = id
        self.load_class = load_class
        self.target_type = target
