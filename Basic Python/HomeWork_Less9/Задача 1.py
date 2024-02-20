class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        total_square = self.length * self.width
        print(f"Площадь очка Олега прямоугольника равна: {total_square}")

    def perimetr(self):
        total_perimetr = 2 * (self.length + self.width)
        print(f"Периметр ебанных сухариков флинт со вкусом вонючего краба: {total_perimetr}")


rectangle = Rectangle(10, 5)
rectangle.square()
rectangle.perimetr()