import numpy as np
from models.fe_model import FeModel
from models.mesh import Mesh
from models.load_step import LoadStep
from models.element_type import *
from models.node import *
from models.element import *
from models.material import *
from models.load_type import *
from models.load import *
from models.result import *
from models.result_type import *

def solve(fe_model: FeModel)->None:
    stiff_matrix = create_stiff_matrix(fe_model)
    for ls in fe_model.load_steps:
        force_vector = np.zeros([len(stiff_matrix[0]), 1])
        mask = apply_loads(fe_model.mesh[0], stiff_matrix, force_vector, ls)
        result = solve_equation(stiff_matrix, force_vector, mask)
        fe_model.results.append(Result(ResultType.TEMPERATURE, ResultTargetType.NODE, ls, result))


def create_stiff_matrix(fe_model: FeModel):
    mesh = fe_model.mesh[0]
    dim_nodes = len(mesh.nodes)
    num_deg_freedom = mesh.elements[0].type.task_type.n_dofs
    mat_k = np.zeros([dim_nodes * num_deg_freedom, dim_nodes * num_deg_freedom])
    dim_elem = len(mesh.elements)
    if num_deg_freedom == 1:
        for elem in mesh.elements:
            local_stif_matrix = local_matrix(elem, num_deg_freedom)
            lm_size = len(local_stif_matrix)
            for j in range(lm_size):
                id1 = mesh.nodes.index(elem.nodes[j])
                for k in range(lm_size):
                    id2 = mesh.nodes.index(elem.nodes[k])
                    mat_k[id1, id2] = mat_k[id1, id2] + local_stif_matrix[j, k]
    else:  # Idk how to assemble matrix with multiple degrees of freedom
        print('Error: please, define global stiffnex matrix for this element type')
    return mat_k


def local_matrix(elem: Element, num_deg_freedom):
    if  (num_deg_freedom == 1):
        hx = abs(elem.nodes[0].coord_x - elem.nodes[1].coord_x)
        hy = abs(elem.nodes[1].coord_y - elem.nodes[2].coord_y)
        param = elem.material.get_property(MaterialProperty.K) / (3 * hx * hy)
        local_stif_matrix = param * np.array([
        [hx ** 2 + hy ** 2, -(-0.5 * hx ** 2 + hy ** 2), -0.5 * (hx ** 2 + hy ** 2), -(hx ** 2 - 0.5 * hy ** 2)],
        [-(-0.5 * hx ** 2 + hy ** 2), hx ** 2 + hy ** 2, -(hx ** 2 - 0.5 * hy ** 2), -0.5 * (hx ** 2 + hy ** 2)],
        [-0.5 * (hx ** 2 + hy ** 2), -(hx ** 2 - 0.5 * hy ** 2), hx ** 2 + hy ** 2, -(-0.5 * hx ** 2 + hy ** 2)],
        [-(hx ** 2 - 0.5 * hy ** 2), -0.5 * (hx ** 2 + hy ** 2), -(-0.5 * hx ** 2 + hy ** 2), hx ** 2 + hy ** 2]])
        return local_stif_matrix
    else:  # Here I wanna create a Gauss integration thing (later)
        print('Error: please, define local stiffnex matrix for this element type')


def apply_loads(mesh: Mesh, K, f, load_step: LoadStep):
    mask = np.ones(len(mesh.nodes), dtype = bool)
    for load in load_step.loads:
        if (load.type.load_class == LoadClass.DIRICHLET) and ( load.value == 0):
            mark_zero_nodes(mesh, mask, load)
        elif load.type.load_class == LoadClass.DIRICHLET:
            apply_dirichlet_load(mesh, K, f, load)
        elif load.type.load_class == LoadClass.VOLUME:
            apply_volume_load(mesh, f, load)
    return mask

def mark_zero_nodes(mesh: Mesh, mask, load: Load):
        for node in load.nodes:
            mask[mesh.nodes.index(node)] = False

def apply_dirichlet_load(mesh: Mesh, K, f, load: Load):
    if (load.value == 0) and (load.type.target_type == LoadTargetType.NODE):
        mask = np.ones(len(mesh.nodes), dtype = bool)
        for node in load.nodes:
            mask[mesh.nodes.index(node)] = False
        K = K[mask, mask]
        f = f[mask]

def apply_volume_load(mesh: Mesh, f, load: Load):
    if load.type.target_type == LoadTargetType.ELEMENT:
        for load_elem in load.elems:
            hx = abs(load_elem.nodes[0].coord_x - load_elem.nodes[1].coord_x)
            hy = abs(load_elem.nodes[1].coord_y - load_elem.nodes[2].coord_y)
            for ne in load_elem.nodes:
                id = mesh.nodes.index(ne)
                f[id] = f[id] + 1/4 * load.value * hx * hy

def solve_equation(mat_k, mat_f,mask):
    reduced_mat_k = mat_k[np.ix_(mask,mask)]
    mat_f = mat_f[np.ix_(mask)]
    dim_k = reduced_mat_k.shape
    dim_f = mat_f.shape
    dim_m = mask.shape
    if (dim_f[0] == dim_k[1]):
        mat_k_reversed = np.linalg.inv(reduced_mat_k)
        reduced_res_t = np.dot(mat_k_reversed, mat_f)
        res_t = np.zeros([dim_m[0], 1])
        k = 0
        for i in range(dim_m[0]):
            if mask[i]:
                res_t[i, 0] = reduced_res_t[k, 0]
                k += 1
        return res_t
    else:
        return None