class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Здарова {self.name} ты уебок ебанный тебе сухарики надо? Ты малолетка {self.age}")


person = Person("Олег", 25)
person.say_hello()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_person(self, other):
        if isinstance(other, Person):
            total_age = self.age + other.age
            return Person("Combined", total_age)
        raise TypeError("Unsupported operand type for add_person")

class Person:
    species = "Human"  # Атрибут класу

    def __init__(self, name):
        self.name = name  # Атрибут об'єкта

