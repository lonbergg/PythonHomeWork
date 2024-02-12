def ім'я_функції(параметри):
    # Тіло функції
    # Виконувані дії
    return результат

def greet(name, message="Hello!"):
    greeting = message + " " + name + "! I'm the greet function."
    print(greeting)

# Виклик функції з передачею тільки обов'язкового аргумента
greet("John")

# Виклик функції з передачею обов'язкового та необов'язкового аргументів
greet("John", "Greetings")

def example(*args):
    for argument in args:
        print(argument)

# Виклик функції з різними аргументами
example("Аргумент1", "Аргумент2", "Аргумент3")


def example(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)

# Виклик функції з різними аргументами
example(name="Олег", age="25", city="Київ")

def get_person_details():
    name = "John"
    age = 25
    city = "New York"
    return name, age, city

person = get_person_details()
print(person)

# Лямбда-функція без аргументів
greet = lambda: "Привіт, світ!"
print(greet())  # Виведе "Привіт, світ!"

# Лямбда-функція з одним аргументом
double = lambda x: x * 2
print(double(5))  # Виведе 10

# Лямбда-функція з більш ніж одним аргументом
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Виведе 12