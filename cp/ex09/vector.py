"""This file contains all the exercises relating to the Vector Exercises (9.4-9.7)."""


class Vector:
    """A class that represents a Vector, defined by the endpoint :math:`(x,y)`."""

    # TODO: Code has been removed from here.

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, v):
        return self.x * v.x + self.y * v.y
