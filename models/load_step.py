from typing import List
from models.load import *
from models.load_step_type import *

class LoadStep:
    def __init__(self, id, name, type: LoadStepType, loads: List[Load], time_point):
        self.id = id
        self.name = name
        self.type = type
        self.loads = loads
        self.time_point = time_point