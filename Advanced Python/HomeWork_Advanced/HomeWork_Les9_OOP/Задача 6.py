import math


class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

    def dlina_kruga(self):
        return 2 * self.pi * self.radius


radius_value = 6
circle_instance = Circle(radius_value)

print(f"Площадь круга:  {radius_value} будет: {circle_instance.area()} ")
print(f"Длина с радиусом: {radius_value} будет: {circle_instance.dlina_kruga()}")