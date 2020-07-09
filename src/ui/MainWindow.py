from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPainter, QPen, QMouseEvent
from PyQt5.QtCore import Qt, QPoint
from .HexagonWidget import HexagonWidget
from src.localization import localization as text

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = text().project_name
        self._initialize_geometry()
        self.setWindowTitle(self.title)
        self.setMouseTracking(True)
        self._initialize_widgets()
        self.show()
        self.start_hexagon_animation()

    def mousePressEvent(self, event: QMouseEvent):
        x = event.x()
        y = event.y()
        self.hexagon_widget.select_hexagon(QPoint(x, y))

    def _initialize_geometry(self):
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)

    def _initialize_widgets(self):
        self._create_hexagon_widget()

    def _create_hexagon_widget(self):
        self.hexagon_widget = HexagonWidget(self)
        self.hexagon_widget.move(0,0)
        self.hexagon_widget.resize(640, 480)

    def start_hexagon_animation(self):
        self._hexagon_circle()
        #self.hexagon_widget.start_animation()

    def _hexagon_circle(self):
        import math
        center_x = 320
        center_y = 240
        radius = 60
        self.hexagon_widget.add_hexagon(center_x, center_y, radius)
        for group in range(1, 4):
            for pos in range(6):
                x = radius * group * 2 * math.cos(math.pi/6 * (pos*2 - 3)) + center_x
                y = radius * group * 2 * math.sin(math.pi/6 * (pos*2 - 3)) + center_y
                self.hexagon_widget.add_hexagon(x, y, radius)
        centers = list(self.hexagon_widget.hexagons)
        for center in centers:
            for pos in range(6):
                x = radius * 2 * math.cos(math.pi/6 * (pos*2 - 3)) + center.x
                y = radius * 2 * math.sin(math.pi/6 * (pos*2 - 3)) + center.y
                self.hexagon_widget.add_hexagon(x, y, radius)

    def set_background_color(self, red: int, green: int, blue: int, alpha: int = 255):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(red, green, blue, alpha))
        self.setPalette(palette)    