import math

class Circle:
    def __init__(self, radius, constanta):
        self.radius = radius
        self.constanta = constanta

    def formyla_square(self):
        s = self.constanta(math.pi) * self.radius**2
        return f"Площадь круга равна {s}"

krug_1 = Circle(6)
print(krug_1)