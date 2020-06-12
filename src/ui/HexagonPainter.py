from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from .Hexagon import Hexagon

class HexagonPainter(QPainter):
    def __init__(self):
        super().__init__()
        
    def begin(self, QPaintDevice):
        super().begin(QPaintDevice)
        self.setRenderHint(QPainter.Antialiasing)

    def drawHexagon(self, hexa: Hexagon, **kwds):
        pen = QPen()
        pen.setWidth(10)
        pen.setJoinStyle(Qt.MiterJoin)
        if ('color' in kwds.keys()):
            pen.setColor(QColor(*kwds['color']))
        else:
            pen.setColor(QColor(*hexa.color))
        self.setPen(pen)
        self.drawPolygon(hexa)