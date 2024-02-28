class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")


class Sedan(Car):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Type: Sedan, Number of Doors: {self.num_doors}")


class SUV(Car):
    def __init__(self, brand, model, num_seats):
        super().__init__(brand, model)
        self.num_seats = num_seats

    def display_info(self):
        super().display_info()
        print(f"Type: SUV, Number of Seats: {self.num_seats}")


class SportsCar(Car):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Type: Sports Car, Max Speed: {self.max_speed} km/h")


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)


sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()