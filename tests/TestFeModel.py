from unittest import TestCase
from unittest.mock import Mock

from models.fe_model import FeModel


class TestFeModel(TestCase):
    def test_apply_material(self):
        mesh = Mock()
        model = FeModel(1, mesh)

        # trivial test case for one entering element

        node_top_left = Mock()
        node_top_left.id = 1
        node_top_left.coord_x = 0
        node_top_left.coord_y = 0

        node_top_right = Mock()
        node_top_right.id = 2
        node_top_right.coord_x = 0
        node_top_right.coord_y = 6

        node_bottom_left = Mock()
        node_bottom_left.id = 3
        node_bottom_left.coord_x = 6
        node_bottom_left.coord_y = 0

        node_bottom_right = Mock()
        node_bottom_right.id = 4
        node_bottom_right.coord_x = 6
        node_bottom_right.coord_y = 6

        region = Mock()
        region.params = [1, 4, 1, 4]

        element = Mock
        element.id = 1
        element.type = 1
        element.material = 2
        element.nodes = [node_top_left, node_top_right, node_bottom_left, node_bottom_right]
        mesh.elements = [
            element
        ]

        # ensure that owr element has the material with id = 2
        self.assertEqual(2, mesh.elements[0].material)

        material = Mock()
        material.id = 3

        model.apply_material(material, region, mesh)
        self.assertEqual(3, mesh.elements[0].material)
