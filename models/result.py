from models.result_type import *
from models.load_step import *

class Result:
    def __init__(self, res_type: ResultType, result_target: ResultTargetType, ls: LoadStep, field):
        self.result_type = res_type
        self.result_target = result_target
        self.ls = ls
        self.field = field
