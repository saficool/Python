from cmath import pi


import math


class Circle:
    _pi = math.pi

    def __init__(self, radius=1) -> None:
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return self._pi*self.radius**2


circle = Circle()
circle.setRadius(3)
print(circle.area())
print(circle.getRadius())
