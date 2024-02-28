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


import random

class Start_Game:
    def __init__(self):
        pass

    def start_option_quit(self):
        while True:
            try:
                start = int(input("Введите число 1 для того чтобы начать игру\n"
                                   "Введите число 2 чтобы узнать характеристики героев\n"
                                   "Введите число 3 если хотите покинуть игру: "))
                if start not in [1, 2, 3]:
                    raise ValueError("Некорректный ввод числа, попробуйте снова!")
                return start
            except ValueError as e:
                print(e)

class Warrior:
    def __init__(self):
        self.HP = 150
        self.Damage = 20
        self.Critical_Damage = 30
        self.Luck = 10

    def display_stats(self):
        return f"Характеристика Warrior(Воин)\n"\
               f"Уровень здоровья HP = {self.HP}\n"\
               f"Базовый Урон Damage = {self.Damage}\n"\
               f"Критический Урон Critical Damage = {self.Critical_Damage}\n"\
               f"Удача Luck = {self.Luck}"

class Archer(Warrior):
    def __init__(self):
        super().__init__()

    def display_stats(self):
        return f"Характеристика Archer(Лучник)\n"\
               f"Уровень здоровья HP = {self.HP}\n"\
               f"Базовый Урон Damage = {self.Damage}\n"\
               f"Критический Урон Critical Damage = {self.Critical_Damage}\n"\
               f"Удача Luck = {self.Luck}"

class Wizard(Warrior):
    def __init__(self):
        super().__init__()

    def display_stats(self):
        return f"Характеристика Wizard(Маг)\n"\
               f"Уровень здоровья HP = {self.HP}\n"\
               f"Базовый Урон Damage = {self.Damage}\n"\
               f"Критический Урон Critical Damage = {self.Critical_Damage}\n"\
               f"Удача Luck = {self.Luck}"

class Rider(Warrior):
    def __init__(self):
        super().__init__()

    def display_stats(self):
        return f"Характеристика Rider(Наездник)\n"\
               f"Уровень здоровья HP = {self.HP}\n"\
               f"Базовый Урон Damage = {self.Damage}\n"\
               f"Критический Урон Critical Damage = {self.Critical_Damage}\n"\
               f"Удача Luck = {self.Luck}"

if __name__ == "__main__":
    game = Start_Game()
    option = game.start_option_quit()

    if option == 1:
        # Реализуйте логику сражений между юнитами
        pass
    elif option == 2:
        warrior = Warrior()
        archer = Archer()
        wizard = Wizard()
        rider = Rider()

        print(warrior.display_stats())
        print(archer.display_stats())
        print(wizard.display_stats())
        print(rider.display_stats())
    else:
        print("Вы покинули игру.")
