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


class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.side_length = side_length

    def display_color(self):
        return f"Color: {self.color}, Side Length {self.side_length}"

    def width(self):
        return self.side_length

    def height(self):
        return self.side_length


shape = Shape("Red")
shape.display_color()  # Виведе "Color: Red"
print(shape.display_color())

rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()  # Виведе "Color: Blue"
print(rectangle.display_color())
print(rectangle.width)  # Виведе 10
print(rectangle.height)  # Виведе 5


square = Square("Green", 8)
square.display_color()  # Виведе "Color: Green"
print(square.display_color())
print(square.width)  # Виведе 8
print(square.height)  # Виведе 8
print(square.side_length)  # Виведе 8