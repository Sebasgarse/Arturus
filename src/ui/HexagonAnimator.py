import threading

class HexagonAnimator:
    def __init__(self, parent):
        self.parent = parent
        self.animation: threading.Thread = None
        self.colors = {
            'blue': [76, 132, 193],
            'red': [255, 76, 132]
        }

    def isRunning(self):
        if (self.animation):
            return True
        return False

    def start_animation(self):
        self.animated_hexagons = {}
        self.animation = self._set_interval(self._animation, 0.1)

    def _set_interval(self, fn, time):
        def func_wrapper():
            self._set_interval(fn, time)
            fn()
        thread = threading.Timer(time, func_wrapper)
        thread.setDaemon(True)
        thread.start()
        return thread

    def _animation(self):
        for hexagon in self.parent.hexagons:
            if (hexagon.id not in self.animated_hexagons.keys()):
                self.animated_hexagons[hexagon.id] = ['red', 0]
            hexagon.color = self._change_hex_color(hexagon)
        self.parent.update()

    def _change_hex_color(self, hexagon):

        def interpolation(x, y):
            o = 0
            if (number_of_frames <= 19):
                o = (y - x) / (20 - number_of_frames)
            return x + o

        if (hexagon.color == self.colors[self.animated_hexagons[hexagon.id][0]]):
            self.animated_hexagons[hexagon.id][0] = [n for n in self.colors.keys() if n != self.animated_hexagons[hexagon.id][0]][0]
            self.animated_hexagons[hexagon.id][1] = 0
        objective_color = self.animated_hexagons[hexagon.id][0]
        number_of_frames = self.animated_hexagons[hexagon.id][1]
        objective_color_rgb = self.colors[objective_color]
        rgb = [
            interpolation(hexagon.color[0], objective_color_rgb[0]),
            interpolation(hexagon.color[1], objective_color_rgb[1]),
            interpolation(hexagon.color[2], objective_color_rgb[2])
        ]
        self.animated_hexagons[hexagon.id][1] += 1
        return rgb