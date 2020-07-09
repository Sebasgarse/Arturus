from PyQt5.QtGui import QPolygon 
import math

class Hexagon(QPolygon):
    number_of_iterations = 0
    def __init__(self, center, x: int, y: int, z: int, radius: int):
        self.id = self.number_of_iterations
        self.local_center = center
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self._initialize_geometry()
        self._color = [76, 132, 193]
        self.line_width = 10
        super().__init__(self.get_area_points())
        self.__class__.number_of_iterations += 1

    def _initialize_geometry(self):
        self.local_x = self.local_center[0] + (self.x * self.get_width()/2) - (self.y * self.get_width()/2)
        self.local_y = self.local_center[1] + (self.z * self.get_height() * 3/4)

    def get_width(self):
        return math.sqrt(3) * self.radius

    def get_height(self):
        return 2 * self.radius

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
            angle = 60 * pos - 30
            angle_rad = math.pi/180 * angle
            x = self.radius * math.cos(angle_rad) + self.local_x
            y = self.radius * math.sin(angle_rad) + self.local_y
            points.append(x)
            points.append(y)
        return points
