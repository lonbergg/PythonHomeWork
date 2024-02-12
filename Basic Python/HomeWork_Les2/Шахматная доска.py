x1 = int(input("Введите число от 1 до 8 "))
x2 = int(input("Введите число от 1 до 8 "))
y1 = int(input("Введите число от 1 до 8 "))
y2 = int(input("Введите число от 1 до 8 "))

color_1 = x1 + x2
color_2 = y1 + y2

if color_1 % 2 == color_2 % 2:
    print(True)
else:
    print(False)
