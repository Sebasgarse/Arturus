from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from .Hexagon import Hexagon

class HexagonPainter(QPainter):
    def __init__(self):
        super().__init__()
        
    def begin(self, QPaintDevice):
        super().begin(QPaintDevice)
        self.setRenderHint(QPainter.Antialiasing)

    def drawHexagon(self, hexagon: Hexagon, **kwds):
        pen = QPen()
        pen.setWidth(hexagon.line_width)
        pen.setColor(QColor(*hexagon.get_color()))
        pen.setJoinStyle(Qt.MiterJoin)
        self.setPen(pen)
        self.drawPolygon(hexagon)