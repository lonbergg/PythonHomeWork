class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


person = Person("John", 30)


person.set_name("NEW_John")
person.set_age(30)


print(person.get_name())
print(person.get_age())