import random


class Start_Game:
    def __init__(self, start, option, quit):
        self.start = start
        self.option = option
        self.quit = quit

    def start_option_quit(self):
        self.start = int(input("Введите число 1 для того чтобы начать игру  \n"
                               "Введите число 2 чтобы узнать характеристики героев  \n"
                               "Введите число 3 если хотите покинуть игру  "))


class Warrior:
    def __init__(self, HP, Damage, Critical_Damage, Luck):
        self.HP = HP
        self.Damage = Damage
        self.Critical_Damage = Critical_Damage
        self.Luck = Luck

    def display_stats(self):
        self.HP = 150
        self.Damage = 20
        self.Critical_Damage = 30
        self.Luck = 10
        print(f"Характеристика Warrior(Воин)\n"
              f"Уровень здоровья HP = {self.HP}\n"
              f"Базовый Урон Damage = {self.Damage}\n"
              f"Критический Урон Critical Damage = {self.Critical_Damage}\n"
              f"Удача Luck = {self.Luck}")


class Archer(Warrior):
    def __init__(self, HP, Damage, Critical_Damage, Luck):
        super().__init__(HP, Damage, Critical_Damage, Luck)

    def display_stats(self):
        self.HP = 140
        self.Damage = 18
        self.Critical_Damage = 35
        self.Luck = 20
        print(f"Характеристика Archer(Лучник)\n"
              f"Уровень здоровья HP = {self.HP}\n"
              f"Базовый Урон Damage = {self.Damage}\n"
              f"Критический Урон Critical Damage = {self.Critical_Damage}\n"
              f"Удача Luck = {self.Luck}")


class Wizard(Warrior):
    def __init__(self, HP, Damage, Critical_Damage, Luck):
        super().__init__(HP, Damage, Critical_Damage, Luck)

    def display_stats(self):
        self.HP = 130
        self.Damage = 25
        self.Critical_Damage = 40
        self.Luck = 15
        print(f"Характеристика Wizard(Маг)\n"
              f"Уровень здоровья HP = {self.HP}\n"
              f"Базовый Урон Damage = {self.Damage}\n"
              f"Критический Урон Critical Damage = {self.Critical_Damage}\n"
              f"Удача Luck = {self.Luck}")


class Rider(Warrior):
    def __init__(self, HP, Damage, Critical_Damage, Luck):
        super().__init__(HP, Damage, Critical_Damage, Luck)

    def display_stats(self):
        self.HP = 160
        self.Damage = 22
        self.Critical_Damage = 25
        self.Luck = 12
        print(f"Характеристика Rider(Наездник)\n"
              f"Уровень здоровья HP = {self.HP}\n"
              f"Базовый Урон Damage = {self.Damage}\n"
              f"Критический Урон Critical Damage = {self.Critical_Damage}\n"
              f"Удача Luck = {self.Luck}")
