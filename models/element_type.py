from enum import Enum
class TaskType(Enum):
    THERMAL_2D = (1, 1)
    THERMAL_3D = (2, 1)
    STRUCTURAL_2D = (3, 2)
    STRUCTURAL_3D = (4, 4)

    def __init__(self, id, n_dofs):
        self.id = id
        self.n_dofs = n_dofs  # number of degrees of freedom


class ElementType(Enum):
    T2T3 = (1, TaskType.THERMAL_2D, 3)
    T2Q4 = (2, TaskType.THERMAL_2D, 4)

    def __init__(self, id, task_type: TaskType, n_nodes):
        self.id = id
        self.task_type = task_type
        self.n_nodes = n_nodes  # number of degrees of freedom
