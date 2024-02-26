class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print("Некорректное имя!")

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age <= 120:
            self.__age = age
        else:
            print("Некоректное значение! Пошел нахуй!")

    def get_age(self):
        return self.__age


person = Person("Алексей", 35)
person.set_name("John123")  # Виведе повідомлення про помилку
person.set_age(150)  # Виведе повідомлення про помилку

print(person.get_name())
print(person.get_age())