class HexagonModificator:
    def __init__(self, parent):
        self.parent = parent
            
    def get_path_of_hexagons(self, hexagon1, hexagon2):
        distance = self.get_distance(hexagon1, hexagon2)
        path_of_hexagons = []
        for step in range(distance):
            t = (step + 1)/distance
            x, y, z = self.hexagon_lerp(hexagon1, hexagon2, t)
            rounded_values = self.round_hexagon(*[x, y, z])
            for hexagon in self.parent.hexagons:
                if rounded_values == hexagon.get_axis_points():
                    path_of_hexagons.append(hexagon)
        return path_of_hexagons

    def show_distance_hexagons(self, hexagon1, hexagon2):
        if not self.parent.hover_hexagon: return
        path_of_hexagons = self.get_path_of_hexagons(hexagon1, hexagon2)
        self._change_hexagons_color_green(*path_of_hexagons)
        self.set_hexagons_to_default(
            *[hexagon for hexagon in self.parent.hexagons 
            if not hexagon in path_of_hexagons 
            and not hexagon is self.parent.selected_hexagon]
            )
        self.parent.update()

    def _change_hexagons_color_green(self, *hexagons):
        for hexagon in hexagons:
            hexagon.set_color(*[13, 132, 77])
            hexagon.priority = True

    def set_hexagons_to_default(self, *hexagons):
        for hexagon in hexagons:
            hexagon.set_default_color()
            hexagon.priority = False

    def hexagon_lerp(self, hexagon1, hexagon2, t):
        x = hexagon1.x + (hexagon2.x - hexagon1.x) * t
        y = hexagon1.y + (hexagon2.y - hexagon1.y) * t
        z = hexagon1.z + (hexagon2.z - hexagon1.z) * t
        return x, y, z

    def get_distance(self, hexagon1, hexagon2):
        x = abs(hexagon1.x - hexagon2.x)
        y = abs(hexagon1.y - hexagon2.y)
        z = abs(hexagon1.z - hexagon2.z)
        total = max(x, y, z)
        return total

    def round_hexagon(self, x, y, z):
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