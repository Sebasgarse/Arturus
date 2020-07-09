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
                self.animated_hexagons[hexagon.id] = {'objective':'red', 'frame':0}
            hexagon.set_color(*self._change_hex_color(hexagon))
        self.parent.update()

    def _change_hex_color(self, hexagon):

        def interpolation(x, y):
            o = 0
            if (number_of_frames <= 19):
                o = (y - x) / (20 - number_of_frames)
            return x + o

        self._verify_finish(hexagon)
        objective_color = self.animated_hexagons[hexagon.id]['objective']
        number_of_frames = self.animated_hexagons[hexagon.id]['frame']
        objective_color_rgb = self.colors[objective_color]
        rgb = [
            interpolation(hexagon.get_color_red(), objective_color_rgb[0]),
            interpolation(hexagon.get_color_green(), objective_color_rgb[1]),
            interpolation(hexagon.get_color_blue(), objective_color_rgb[2])
        ]
        self.animated_hexagons[hexagon.id]['frame'] += 1
        return rgb

    def _verify_finish(self, hexagon):
        objective_color = self.animated_hexagons[hexagon.id]['objective']
        if (hexagon.get_color() == self.colors[objective_color]):
            next_objective_color = [n for n in self.colors.keys() if n != objective_color][0]
            self.animated_hexagons[hexagon.id]['objective'] = next_objective_color
            self.animated_hexagons[hexagon.id]['frame'] = 0
