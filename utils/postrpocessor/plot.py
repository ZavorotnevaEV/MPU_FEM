import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np
from models.mesh import Mesh
from models.result import Result
from models.mesh_params import MeshParams

def plot_result_on_rect_mesh(result: Result, mesh: Mesh, mesh_params: MeshParams):
    k=0
    m=mesh_params.divisions[0] + 1
    n=mesh_params.divisions[1] + 1
    x = np.zeros((m, n))
    y = np.zeros((m, n))
    z = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            x[i, j] = mesh.nodes[k].coord_x
            y[i, j] = mesh.nodes[k].coord_y
            z[i, j] = result.field[k]
            k += 1
    plt.contourf(x, y, z, 20,cmap = 'gist_gray')
    plt.axis('scaled')
    plt.colorbar()
    plt.show()