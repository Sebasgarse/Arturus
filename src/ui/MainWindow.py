from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPainter, QPen
from PyQt5.QtCore import Qt
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

    def _initialize_geometry(self):
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)

    def _initialize_widgets(self):
        self._create_hexagon_widget()
        self.button = QPushButton(text().start, self)
        self.button.move(0, 0)
        self.button.clicked.connect(self.start_hexagon_animation)

    def _create_hexagon_widget(self):
        self.hexagon_widget = HexagonWidget(self)
        self.hexagon_widget.move(100,200)
        self.hexagon_widget.resize(500, 300)

    def start_hexagon_animation(self):
        x = 60 * (len(self.hexagon_widget.hexagons) + 1)
        y = 70
        self.hexagon_widget.add_hexagon(x, y, 60)
        if (not self.hexagon_widget.isAnimating()):
            self.hexagon_widget.start_animation()

    def set_background_color(self, red: int, green: int, blue: int, alpha: int):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(red, green, blue, 255))
        self.setPalette(palette)    