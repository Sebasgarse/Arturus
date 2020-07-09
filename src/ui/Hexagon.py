from PyQt5.QtGui import QPolygon 
import math

class Hexagon(QPolygon):
    number_of_iterations = 0
    def __init__(self, x: int, y: int, radius: int):
        self.id = self.number_of_iterations
        self.x = x
        self.y = y
        self.radius = radius
        self._color = [76, 132, 193]
        self.line_width = 10
        super().__init__(self.get_area_points())
        self.__class__.number_of_iterations += 1

    def set_color(self, red:int, green:int, blue:int):
        self._color = [red, green, blue]

    def set_default_color(self):
        self._color = [76, 132, 193]

    def get_color(self):
        return self._color

    def get_color_red(self):
        return self._color[0]

    def get_color_green(self):
        return self._color[1]

    def get_color_blue(self):
        return self._color[2]

    def get_area_points(self):
        points = []
        for pos in range(6):
            x = self.radius * math.cos(math.pi/3 * pos) + self.x
            y = self.radius * math.sin(math.pi/3 * pos) + self.y
            points.append(x)
            points.append(y)
        return points
