a = int(input("Введите количество учеников 1 класса: "))
b = int(input("Введите количество учеников 2 класса: "))
c = int(input("Введите количество учеников 3 класса: "))

first_class = a // 2 + a % 2
second_class = b // 2 + b % 2
third_class = c // 2 + c % 2

vse_parti = first_class + second_class + third_class

print(f"Количество парт необходимое для учеников: {vse_parti}")