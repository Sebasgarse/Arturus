from PyQt5.QtWidgets import QWidget
from .Hexagon import Hexagon
from .HexagonPainter import HexagonPainter
from .HexagonAnimator import HexagonAnimator

class HexagonWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.hexagons = []
        self._hexagon_animator = HexagonAnimator(self)
        
    def paintEvent(self, event):
        painter = HexagonPainter()
        painter.begin(self)
        for hexagon in self.hexagons:
            painter.drawHexagon(hexagon)
        painter.end()

    def add_hexagon(self, x:int, y:int, radius:int):
        if ([x, y] in [[n.x, n.y] for n in self.hexagons]):
            return 
        hexa = Hexagon(x,  y, radius)
        self.hexagons.append(hexa)
        self.update()

    def start_animation(self):
        self._hexagon_animator.start_animation()

    def isAnimating(self):
        return self._hexagon_animator.isRunning()
        
