import numpy as np
from models.region_type import RegionType


# Пока не придумал ничего лучше испольования трех типов регионов.
# (Линия паралл оси X, линия паралл оси Y и прямоугольник)
# Можно было бы описать линию координатами крайних точек, но уровнем получается проще для пользователя.
# Здесь Type - это класс Region Type (т.е. где-то нужно будет создавать типы)
# Если тип rectangle, то params задается как [x1, y1, x2, y2]
class Region:
    def __init__(self, id, name, type: RegionType, params):
        self.id = id
        self.name = name
        self.type = type
        self.params = params



