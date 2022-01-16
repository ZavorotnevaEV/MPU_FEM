# ---Основной файл---#

import utils.postrpocessor.plot as plot
import utils.solver as solver
from models.element_type import *
# ---Импортируйте сюда свои библиотеки---#
from models.fe_model import FeModel
from models.load_step import *
from models.load_step_type import *
from models.material import *
from models.material_property import *
from models.material_type import *
from models.mesh_params import MeshParams
from models.mesh_type import *
from models.property import Property
from models.region_type import RegionType
from utils.preprocessor import cad, mesher, load_utils

rect1 = cad.create_rectangle(1, "Rectangle1", 0, 1, 0, 1)
pid1 = Property(1, 'pid1')
mat1 = Material(1, 'Steel', MaterialType.THERMAL_ISOTROPIC)
mat1.set_property(MaterialProperty.K, 16)
mesh_params = MeshParams(1, rect1, pid1, ElementType.T2T3, mat1, [10, 10], MeshType.MAP)
mesh1 = mesher.rect_mesh(mesh_params)
line_y = Region(1, "liney", RegionType.LINE_Y, [0])
load2 = load_utils.create_load_by_region(1, "fix_line_y", mesh1, LoadType.TEMP, line_y, 0)
rect2 = Region(2, "hetgen", RegionType.RECTANGLE, [0, 1, 0, 1])
load1 = load_utils.create_load_by_region(1, "heat_gen", mesh1, LoadType.HEATGEN, rect2, 100)
ls1 = LoadStep(1, "thermal_static", LoadStepType.STATIC, [load1, load2], 1)




model1 = FeModel(1)
model1.geometry.append(rect1)
model1.mesh.append(mesh1)
model1.mesh_params.append(mesh_params)
model1.load_steps.append(ls1)
solver.solve(model1)
plot.plot_result_on_rect_mesh(model1.results[0], model1.mesh[0], model1.mesh_params[0])



