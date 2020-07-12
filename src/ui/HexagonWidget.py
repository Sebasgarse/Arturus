from PyQt5.QtWidgets import QWidget
from .Hexagon import Hexagon
from .HexagonModificator import HexagonModificator
from .HexagonPainter import HexagonPainter
from .HexagonAnimator import HexagonAnimator

class HexagonWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.hexagons = []
        self._hexagon_animator = HexagonAnimator(self)
        self._hexagon_modificator = HexagonModificator(self)
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
                    self._hexagon_modificator.set_hexagons_to_default(*[hexagon for hexagon in self.hexagons if not hexagon is self.selected_hexagon])
                self.selected_hexagon = hexagon
                hexagon.set_color(*[13, 132, 77])
                self.update()

    def distance_hexagon(self, point):
        if self.selected_hexagon:
            self._get_hover_hexagon(point)
            self._hexagon_modificator.show_distance_hexagons(self.selected_hexagon, self.hover_hexagon)

    def _get_hover_hexagon(self, point):
        self.hover_hexagon = None
        for hexagon in self.hexagons:
            if hexagon.containsPoint(point, 0):
                self.hover_hexagon = hexagon
                break

    def start_animation(self):
        self._hexagon_animator.start_animation()

    def isAnimating(self):
        return self._hexagon_animator.isRunning()