from enum import Enum

class ResultTargetType(Enum):
    NODE = 1
    ELEMENT = 2

class ResultType(Enum):
    TEMPERATURE = 1
    THERMAL_FLUX = 2
