from PyQt5.QtWidgets import QWidget
from .Hexagon import Hexagon
from .HexagonPainter import HexagonPainter
from .HexagonAnimator import HexagonAnimator

class HexagonWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.hexagons = []
        self._hexagon_animator = HexagonAnimator(self)
        self.selected_hexagon = None
        self._axis_center = None
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = HexagonPainter()
        painter.begin(self)
        for hexagon in self.hexagons:
            painter.drawHexagon(hexagon)
        if self.selected_hexagon:
            painter.drawHexagon(self.selected_hexagon)
        for hexagon in [hexagon for hexagon in self.hexagons if hexagon.priority]:
            painter.drawHexagon(hexagon)
        painter.end()

    def set_axis_center(self, x, y):
        self._axis_center = [x, y]

    def add_hexagon(self, x:int, y:int, z:int, radius:int):
        if not self._axis_center:
            return
        if self._hexagon_already_exists(x, y, z):
            return
        hexa = Hexagon(self._axis_center, x, y, z, radius)
        self.hexagons.append(hexa)
        self.update()

    def _hexagon_already_exists(self, x: int, y: int, z: int):
        if [x, y, z] in [[hexagon.x, hexagon.y, hexagon.z] for hexagon in self.hexagons]:
            return true

    def select_hexagon(self, point):
        for hexagon in self.hexagons:
            if hexagon.containsPoint(point, 0):
                if self.selected_hexagon:
                    self.selected_hexagon.set_default_color()
                self.selected_hexagon = hexagon
                hexagon.set_color(*[13, 132, 77])
                self.update()

    def distance_hexagon(self, point):
        if self.selected_hexagon:
            hover_hexagon = None
            for hexagon in self.hexagons:
                if hexagon.containsPoint(point, 0):
                    hover_hexagon = hexagon
                    break
            if hover_hexagon:
                distance = self._get_distance(hover_hexagon)
                hexagons_distance = self._get_hexagons_distance(hover_hexagon, distance)
                for hex_dis in hexagons_distance:
                    hex_dis.set_color(*[13, 132, 77])
                    hex_dis.priority = True
                for hexagon in self.hexagons:
                    if not hexagon in hexagons_distance and not hexagon is self.selected_hexagon:
                        hexagon.set_default_color()
                        hexagon.priority = False
                self.update()

    def _get_distance(self, hexagon):
        h1 = self.selected_hexagon
        h2 = hexagon
        x = abs(h1.x - h2.x)
        y = abs(h1.y - h2.y)
        z = abs(h1.z - h2.z)
        total = max(x, y, z)
        return total

    def _get_hexagons_distance(self, hexagon, distance):
        h1 = self.selected_hexagon
        h2 = hexagon
        hexagons_distance = []
        for step in range(distance):
            t = (step + 1)/distance
            x = int(h1.x + (h2.x - h1.x) * t)
            y = int(h1.y + (h2.y - h1.y) * t)
            z = int(h1.z + (h2.z - h1.z) * t)
            for hexagon in self.hexagons:
                if self._round_hexagon(*[x, y, z]) == hexagon.get_axis_points():
                    hexagons_distance.append(hexagon)
        return hexagons_distance

    def _round_hexagon(self, x, y, z):
        rx = round(x)
        ry = round(y)
        rz = round(z)
        x_diff = abs(rx - x)
        y_diff = abs(ry - y)
        z_diff = abs(rz - z)
        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry-rz
        elif y_diff > z_diff:
            ry = -rx-rz
        else:
            rz = -rx-ry
        return [rx, ry, rz]

    def start_animation(self):
        self._hexagon_animator.start_animation()

    def isAnimating(self):
        return self._hexagon_animator.isRunning()
        
