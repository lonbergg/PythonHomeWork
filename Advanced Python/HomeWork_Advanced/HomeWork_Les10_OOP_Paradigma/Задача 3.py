class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, distance):
        self.mileage += distance
        limit_miliage = 300000
        if self.mileage > limit_miliage:
            print("Достижение лимита")


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())  # Виведе "Toyota"
print(car.get_model())  # Виведе "Camry"
print(car.get_year())  # Виведе 2020
print(car.get_mileage())  # Виведе 5000

car.drive(100)  # Збільшення пробігу на 100
print(car.get_mileage())  # Виведе 5100

car.drive(300000)  # Виведе повідомлення про досягнення ліміту