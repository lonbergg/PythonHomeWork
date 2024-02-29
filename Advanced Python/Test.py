# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 24, 26, 63, 72, 91, 72, 72]
#
# # peremennay = tuple(map(is_even, my_list))
# #
# # syhariki = tuple(filter(is_even, my_list))
# # print(syhariki)
#
# def my_filter(function, iterable):
#     res = []
#     for i in iterable:
#         if function(i) is True:
#             res.append(i)
#     switch = set(res)
#     switch_2 = list(switch)
#     switch_2.sort()
#     return switch_2
#
# print(my_filter(is_even, my_list))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# def my_filter (func, iterable):
#     res = []
#     for i in iterable:
#         if func(i) is True:
#             res.append(i)
#     switch = set(res)
#     switch1 = list(switch)
#     switch2 = switch1.sort()
#     return switch2

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# def my_filter(function, iterable):
#     res = []
#     for i in iterable:
#         if function(i) is True:
#             res.append(i)
#     switch = set(res)
#     switch1 = list(switch)
#     switch2 = switch1.sort()
#     return switch2
#
# print(my_filter(is_even, my_list))


# file = open('file.txt', 'r')
# content = file.read()
# print(content)
# file.close()

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
                start = int(input("Введите число от 1-3 чтобы выбрать действие: "))
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
               f"Удача Luck = {self.luck}\n"


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
               f"Удача Luck = {self.luck}\n"


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
               f"Удача Luck = {self.luck}\n"


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
               f"Удача Luck = {self.luck}\n"


game = Menu()
option = game.game_start()

if option == 1:

    pass
elif option == 2:
    warrior = Warrior(150, 20, 30, 10)
    archer = Archer(140, 18, 35, 20)
    wizard = Wizard(130, 25, 40, 15)
    rider = Rider(160, 22, 25, 12)

    print(warrior.display_stats())
    print(archer.display_stats())
    print(wizard.display_stats())
    print(rider.display_stats())
else:
    print("Вы покинули игру.")

