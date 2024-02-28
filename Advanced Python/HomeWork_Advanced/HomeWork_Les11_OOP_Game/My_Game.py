import random


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def game_start():
        while True:
            try:
                print("1. Начать игру")
                print("2. Узнать характеристики героев")
                print("3. Покинуть игру")
                start = int(input("Введите число от 1-3 чтобы выбрать действие"))
                if start not in [1, 2, 3]:
                    raise ValueError("Некорректный ввод числа, попробуйте снова!")
                return start
            except ValueError as e:
                print(e)


class Warrior:
    def __init__(self, hp, damage, critical_damage, luck):
        self.hp = hp
        self.damage = damage
        self.critical_damage = critical_damage
        self.luck = luck

    def display_stats(self):
        self.hp = 150
        self.damage = 20
        self.critical_damage = 30
        self.luck = 10
        return f"Характеристика Warrior(Воин)\n" \
               f"Уровень здоровья HP = {self.hp}\n" \
               f"Базовый Урон Damage = {self.damage}\n" \
               f"Критический Урон Critical Damage = {self.critical_damage}\n" \
               f"Удача Luck = {self.luck}"


class Archer(Warrior):
    def __init__(self, hp, damage, critical_damage, luck):
        super().__init__(hp, damage, critical_damage, luck)

    def display_stats(self):
        self.hp = 140
        self.damage = 18
        self.critical_damage = 35
        self.luck = 20
        return f"Характеристика Archer(Лучник)\n" \
               f"Уровень здоровья HP = {self.hp}\n" \
               f"Базовый Урон Damage = {self.damage}\n" \
               f"Критический Урон Critical Damage = {self.critical_damage}\n" \
               f"Удача Luck = {self.luck}"


class Wizard(Warrior):
    def __init__(self, hp, damage, critical_damage, luck):
        super().__init__(hp, damage, critical_damage, luck)

    def display_stats(self):
        self.hp = 130
        self.damage = 25
        self.critical_damage = 40
        self.luck = 15
        return f"Характеристика Wizard(Маг)\n" \
               f"Уровень здоровья HP = {self.hp}\n" \
               f"Базовый Урон Damage = {self.damage}\n" \
               f"Критический Урон Critical Damage = {self.critical_damage}\n" \
               f"Удача Luck = {self.luck}"


class Rider(Warrior):
    def __init__(self, hp, damage, critical_damage, luck):
        super().__init__(hp, damage, critical_damage, luck)

    def display_stats(self):
        self.hp = 160
        self.damage = 22
        self.critical_damage = 25
        self.luck = 12
        return f"Характеристика Rider(Наездник)\n" \
               f"Уровень здоровья HP = {self.hp}\n" \
               f"Базовый Урон Damage = {self.damage}\n" \
               f"Критический Урон Critical Damage = {self.critical_damage}\n" \
               f"Удача Luck = {self.luck}"


warrior = Warrior
archer = Archer
wizard = Wizard
rider = Rider
