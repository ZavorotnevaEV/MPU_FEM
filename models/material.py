from models.material_type import MaterialType
from models.material_property import MaterialProperty
from typing import Dict


class Material():
    def __init__(self, id, name, type: MaterialType):
        self.id = id
        self.name = name
        self.type = type
        self.properties = {}

    def set_property(self, mat_prop: MaterialProperty, value):
        if mat_prop.value in self.type.mat_props:
            self.properties[mat_prop] = value
        else:
            print('Error:' + mat_prop.name + ' property is not supported by ' + self.type.name + 'material type')

    def get_property(self, mat_prop: MaterialProperty):
        if mat_prop in self.properties.keys():
            return self.properties.get(mat_prop)
        else:print('Error:' + mat_prop.name + ' property is not specified for ' + self.type.name + ' material type')




