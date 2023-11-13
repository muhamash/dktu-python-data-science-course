"""The Rectangle-exercises 9.1-9.3."""


from cp.ex09.vector import Vector


class Rectangle:
    """A class that represents a Rectangle."""

    # TODO: Code has been removed from here.
    def __init__(self, width, height, x_c=0, y_c=0):
        self.width = width
        self.height = height
        self.x_c = x_c
        self.y_c = y_c

    def translate(self, v):
        self.x_c += v.x
        self.y_c += v.y


r = Rectangle(2, 2, 1, 1)
print((r.x_c, r.y_c))

r.translate(Vector(1, 1))
print((r.x_c, r.y_c))
