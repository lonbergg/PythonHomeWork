# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Дарова меня зовут {self.name}, мне {self.age}")
#
#
# person = Person("Олег", 306)
#
# person.greet()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def _get_age(self):
#         return self.age
#
# person = Person("Jown", 306)
#
# print(person._get_age())

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __get_age(self):
#         return self.__age
#
#
# person = Person("Okeg", 406)
#
# try:
#     print(person.__get_age())
# except AttributeError:
#     print("Пошел нахуй")
#
#
#     class Person:
#         def __init__(self, name, age):
#             self.__name = name
#             self.__age = age
#
#         def __get_age(self):
#             return self.__age
#
#
#     # Створимо об'єкт класу Person
#     person = Person("John", 25)
#
#     # Намагаємося викликати приватний метод
#     try:
#         print(person.__get_age())
#     except AttributeError:
#         print("Cannot access private method.")  # Очікуваний вивід: "Cannot access private method."
#
#     # А тепер спробуємо "обійти" приватність
#     try:
#         print(person._Person__get_age())  # Очікуваний вивід: 25
#     except AttributeError:
#         print("Cannot access private method.")


# class ChildClass(ParentClass):
# class Animal:
#         def sound(self):
#             print("animal makes sound")
#
#
# class Dog(Animal):
#         def bark(self):
#             print("Dog barks")
#
#
#
# dog = Dog()
# dog.sound()  # Виклик методу sound успадкованого від Animal
# dog.bark()  # Виклик методу bark в класі Dog

# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):
#         print(f"Привет я {self.name}")
#
# class Child(Parent):
#
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def say_hello(self):
#         super().say_hello()
#         print(f"Здарова {self.age}")
#
#
# child = Child("Sanya", 200)
# child.say_hello()

# class ChildClass(ParentClass1, ParentClass2, ...):
#     # Власний код класу-

# class A:
#     def say_hello(self):
#         print("Hello from A")
#
# class B:
#     def say_hello(self):
#         print("Hello from B")
#
# class C(A, B):
#     pass
#
# c = C()
# c.say_hello()

class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


def animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sound(dog)  # Виведе: Woof!
animal_sound(cat)  # Виведе: Meow!