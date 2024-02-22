class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed


car_1 = Vehicle("BMW", 280, 20000)
car_2 = Vehicle("Ford", 250, 15000)
print(car_1.__gt__(car_2))

my_list_cars = [
    Vehicle("Kia", 220, 12000),
    Vehicle("PRIORA", 840, 2000),
    Vehicle("Hyundai", 200, 13000),
    Vehicle("Tesla", 180, 14500)
]

cars_sort = sorted(my_list_cars, key=lambda car: car.speed)
for car in cars_sort:
    print(f"{car.name} - Скорость ебучая: {car.speed}")