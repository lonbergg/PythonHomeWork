class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_color(self):
        return f"Color: {self.color}, Width: {self.width}, Height: {self.height}"


shape = Shape("Red")
shape.display_color()  # Виведе "Color: Red"
print(shape.display_color())

rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()  # Виведе "Color: Blue"
print(rectangle.display_color())
print(rectangle.width)  # Виведе 10
print(rectangle.height)  # Виведе 5