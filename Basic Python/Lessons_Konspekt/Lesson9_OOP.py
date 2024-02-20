class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Здарова {self.name} ты уебок ебанный тебе сухарики надо? Ты малолетка {self.age}")


person = Person("Олег", 25)
person.say_hello()