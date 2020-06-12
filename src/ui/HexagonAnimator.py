import threading

class HexagonAnimator:
    def __init__(self, parent):
        self.parent = parent

    def start_animation(self):
        self.anim_value = 0
        self.anim_objective = [193, 76, 132]
        self.anim = self._set_interval(self._animation, 0.1)

    def _set_interval(self, fn, time):
        def func_wrapper():
            self._set_interval(fn, time)
            fn()
        t = threading.Timer(time, func_wrapper)
        t.start()
        return t

    def _animation(self):
        if (self.anim_value == 20):
            self.set_animation_color()
            self.anim_value = 0
        for hexa in self.parent.hexagons:
            hexa.color = self.vector3_interpolation_10(*hexa.color, *self.anim_objective)
        self.parent.update()

    def set_animation_color(self):
        if (self.anim_objective == [193, 76, 132]):
            self.anim_objective = [76, 132, 193]
        else:
            self.anim_objective = [193, 76, 132]

    def vector3_interpolation_10(self, x1, y1, z1, x2, y2, z2):
        def vector_interpolation(x, y):
            o = (y - x) / (20 - self.anim_value)
            return x + o
        vector3 = []
        vector3.append(vector_interpolation(x1, x2))
        vector3.append(vector_interpolation(y1, y2))
        vector3.append(vector_interpolation(z1, z2))
        self.anim_value += 1
        return vector3