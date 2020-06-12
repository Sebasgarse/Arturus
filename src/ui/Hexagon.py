from PyQt5.QtGui import QPolygon 
import math

class Hexagon(QPolygon):
    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = [76, 132, 193]
        super().__init__(self.get_area_points())

    def get_area_points(self):
        points = []
        for pos in range(6):
            x = self.radius * math.cos(math.pi/3 * pos) + self.x
            y = self.radius * math.sin(math.pi/3 * pos) + self.y
            points.append(x)
            points.append(y)
        return points
