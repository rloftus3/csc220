import point
import color

class Circle:
    def __init__(self, center, radius, fill):
        self._center = center
        self._radius = radius
        self._fill = fill

    def get_center(self):
        return self._center

    def set_center(self, c):
        self._center = c

    def get_radius(self):
        return self._radius

    def set_radius(self, r):
        self._radius = r

    def get_fill(self):
        return self._fill

    def set_fill(self, f):
        self._fill = f

    def html(self):
        c = self._center
        cx = c.get_across()
        cy = c.get_down()
        return f"""<circle r="{self._radius}" cx="{cx}" cy="{cy}" fill="{self._fill.rgb()}"/>"""

    def __repr__(self):
        return f"<{self._center}, {self._radius}, {self._fill}>"

# unit testing 
if __name__ == "__main__":
    p1 = point.Point(40, 25)
    r = 4
    f = color.Color(40, 255, 0)
    c = Circle(p1, r, f)
    print(c.html())
    print(c)