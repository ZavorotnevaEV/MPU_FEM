from typing import List
from models.material import Material
from models.mesh import Mesh
from models.region import Region
from models.load import Load
from models.load_step import LoadStep
from models.mesh_params import MeshParams
from models.geometry import Geometry
from models.element_type import TaskType
from models.property import Property
from models.result import Result


class FeModel:
    def __init__(self, id, task_type: TaskType=None, geometry: List[Geometry]=[], mesh: List[Mesh]=[], 
                 mesh_params: List[MeshParams]=[], pids: List[Property]=[],
                 materials: List[Material]=[], loads: List[Load]=[], load_steps: List[LoadStep]=[],
                 regions: List[Region]=[], results: List[Result]=[]):
        self.id = id
        self.task_type = task_type
        self.geometry = geometry
        self.mesh = mesh
        self.mesh_params = mesh_params
        self.pids = pids
        self.materials = materials
        self.loads = loads
        self.load_steps = load_steps
        self.regions = regions
        self.results = results


    def get_material_by_id(self, id):
        for material in self.materials:
            if material.id == id:
                return material


    def add_load_case(self, Id, Name, BCs, Loads):  # добавление LoadCase с последующей записью в файл
        loadC = LoadStep(Id, Name, BCs, Loads)
        self.load_steps.append(loadC)
        with open("../utils/LoadCase.txt", 'a') as file_out:
            file_out.write(str(Id) + " " + str(Name) + " " + str(BCs) + " " + str(Loads) + "\n")

    def import_load_case(self):  # импортирование LoadCase из файла
        Load_Case_Number = {}
        lines = 0
        with open("../utils/LoadCase.txt", "r") as file_out:
            for line in file_out:
                lines = lines + 1
        file_out.close()
        with open("../utils/LoadCase.txt", "r") as file_out:
            for i in range(lines):
                Load_Case_Number[i] = file_out.readline().split()
                loadC = LoadStep(Load_Case_Number[i][0], Load_Case_Number[i][1], Load_Case_Number[i][2],
                                Load_Case_Number[i][3])
                self.load_steps.append(loadC)
        file_out.close()




