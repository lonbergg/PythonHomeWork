class Animal:
    def __init__(self, name, vid_name):
        self.name = name
        self.vid_name = vid_name

    def get_name(self):
        return self.name

    def get_vid_name(self):
        return self.vid_name


class Mammal(Animal):
    def __init__(self, name, vid_name, herbivore):
        super().__init__(name, vid_name)
        self.herbivore = herbivore

    def display_info(self):
        print(f"Name: {self.name}, \nType: {self.vid_name}, \nHerbivore: {self.herbivore}")


class Carnivore(Mammal):
    def __init__(self, name, vid_name, herbivore, teeth):
        super().__init__(name, vid_name, herbivore)
        self.teeth = teeth

    def display_info(self):
        super().display_info()
        print(f"Teeth: {self.teeth}")


class Lion(Carnivore):
    def __init__(self, name, vid_name, herbivore, teeth, mane):
        super().__init__(name, vid_name, herbivore, teeth)
        self.mane = mane

    def display_info(self):
        super().display_info()
        print(f"Mane: {self.mane}")


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()