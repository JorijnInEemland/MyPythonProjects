# Some python class related homework

import math


class Point:
    """Two values"""

    def __init__(self, *args):
        if len(args) == 2:
            if all(a for a in args if type(a) == float):
                self.x = args[0]
                self.y = args[1]

        elif len(args) == 1:
            if type(args[0]) == Point:
                self.x = args[0].x
                self.y = args[0].y

        else:
            self.x = 0.0
            self.y = 0.0

class Line:
    """Two points"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def distance(self):
        return (((self.b.x - self.a.x) ** 2.0) + ((self.b.y - self.a.y) ** 2.0)) ** 0.5


a = Point()
b = Point(0.0, 1.0)
c = Point(b)

l = Line(a, c)
print(l.distance())
