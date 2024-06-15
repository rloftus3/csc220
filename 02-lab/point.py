class Point:
    def __init__(self, across = 0, down = 0):
        self._across = across
        self._down = down

    def get_across(self):
        return self._across

    def set_across(self, a):
        self._across = a

    def get_down(self):
        return self._down

    def set_down(self, d):
        self._down = d
    
    def __repr__(self):
        return f"<{self._across}, {self._down}>"

# unit testing 
if __name__ == "__main__":
    p1 = Point()
    print(p1)
    x = p1.get_across()
    print(x)