class Color:
    def __init__(self, red = 0, green = 0, blue = 0):
        self._red = red
        self._green = green
        self._blue = blue

    def get_red(self):
        return self._red

    def set_red(self, r):
        self._red = r

    def get_green(self):
        return self._green

    def set_green(self, g):
        self._green = g

    def get_blue(self):
        return self._blue

    def set_blue(self, b):
        self._blue = b

    def rgb(self):
        return f"rgb({self._red}, {self._green}, {self._blue})"
    
    def __repr__(self):
        return f"<{self._red}, {self._green}, {self._blue}>"

# unit testing 
if __name__ == "__main__":
    p1 = Color()
    print(p1)