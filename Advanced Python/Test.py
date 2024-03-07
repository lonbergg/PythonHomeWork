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
from enum import Enum
import sys
import time


class CharacterType(Enum):
    WARRIOR = 0
    ARCHER = 1
    WIZARD = 2
    RIDER = 3


class Character:
    def __init__(self, name, hp, damage, critical_damage, luck, level):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        self.critical_damage = critical_damage
        self.luck = luck
        self.level = level

    def display_options(self):
        return print(f"Характеристика героя \n"
                     f"Hero: {self.name}\n"
                     f"Уровень здоровья HP = {self.hp}\n"
                     f"Базовый Урон Damage = {self.damage}\n"
                     f"Критический Урон Critical Damage = {self.critical_damage}\n"
                     f"Удача Luck = {self.luck}\n"
                     f"Уровень Level = {self.level}\n")

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage * self.critical_damage)
            print(f'----- {crit} CRITICAL DAMAGE -----')
            return crit
        else:
            return self.damage

    def level_up(self):
        self.level += 1
        self.max_hp += 15
        self.hp = self.max_hp
        self.damage += 5
        self.critical_damage += 0.10
        self.luck += 3

    def reset_hp(self):
        self.hp = self.max_hp


class Warrior(Character):
    def __init__(self):
        super().__init__("Warrior", 150, 20, 0.3, 10, 1)

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            return self.dmg() + (self.damage * 0.15)
        return self.dmg()


class Archer(Character):
    def __init__(self):
        super().__init__("Archer", 140, 18, 0.35, 20, 1)

    def attack(self, enemy):
        if isinstance(enemy, Rider):
            return self.dmg() + (self.damage * 0.15)
        return self.dmg()


class Wizard(Character):
    def __init__(self, ):
        super().__init__("Wizard", 130, 25, 0.40, 15, 1)

    def attack(self, enemy):
        if isinstance(enemy, Archer):
            return self.dmg() + (self.damage * 0.15)
        return self.dmg()


class Rider(Character):
    def __init__(self, ):
        super().__init__("Rider", 160, 22, 0.25, 12, 1)

    def attack(self, enemy):
        if isinstance(enemy, Warrior):
            return self.dmg() + (self.damage * 0.15)
        return self.dmg()


def char(char_type: CharacterType):
    char_dict = {
        CharacterType.WARRIOR: Warrior,
        CharacterType.ARCHER: Archer,
        CharacterType.WIZARD: Wizard,
        CharacterType.RIDER: Rider
    }
    return char_dict[char_type]()


characters = [char(CharacterType.WARRIOR),
              char(CharacterType.ARCHER),
              char(CharacterType.WIZARD),
              char(CharacterType.RIDER)]


class Game:

    def game_start(self):
        while True:
            print("1. Начать игру")
            print("2. Покинуть игру")
            choose = int(input("Введите число от 1-2 чтобы выбрать действие: "))
            match choose:
                case 1:
                    self.start_game()
                case 2:
                    sys.exit()
                case _:
                    print("Incorrect input, please try again")
                    self.game_start()

    @staticmethod
    def select_character():
        print("| Выберите своего игрового персонажа          |")
        print("| Введите 1 для выбора =====> Warrior(Воин)   |")
        print("| Введите 2 для выбора =====> Archer(Лучник)  |")
        print("| Введите 3 для выбора =====> Wizard(Маг)     |")
        print("| Введите 4 для выбора =====> Rider(Наездник) |")

        choose = int(input("Введите число от 1-4 чтобы выбрать действие: "))
        match choose:
            case 1:
                choose = characters[0]
            case 2:
                choose = characters[1]
            case 3:
                choose = characters[2]
            case 4:
                choose = characters[3]
            case _:
                print("Некоректный выбор! Персонаж не выбран! Попробуй снова!")
        return choose

    @staticmethod
    def fight_hero(hero_1, hero_2):
        print(f"Битва {hero_1.name} vs {hero_2.name} Valhalla Coming For YOU BITCH! ")
        print(f"Fight!\n")
        while hero_1.hp > 0 and hero_2.hp > 0:
            print(f"{hero_1.name} сражается с {hero_2.name}!")
            damage_dealt = hero_1.dmg()
            hero_2.hp -= damage_dealt
            print(f"{hero_1.name} наносит {damage_dealt} урона.")
            print('<--------------------------------------------->')
            time.sleep(2)
            if hero_2.hp <= 0:
                print(f"{hero_2.name} погибает. {hero_1.name} побеждает!")

            print(f"{hero_2.name} сражается с {hero_1.name}!")
            damage_dealt = hero_2.dmg()
            hero_1.hp -= damage_dealt
            print(f"{hero_2.name} наносит {damage_dealt} урона.")
            time.sleep(2)
            print('<--------------------------------------------->')
            if hero_1.hp <= 0:
                print(f"{hero_1.name} погибает. {hero_2.name} побеждает!")

            print(f"\nТекущее здоровье {hero_1.name}: {hero_1.hp}")
            print(f"Текущее здоровье {hero_2.name}: {hero_2.hp}\n")

        if hero_1.hp > 0:
            print(f"{hero_1.name} побеждает!")
        elif hero_2.hp > 0:
            print(f"{hero_2.name} побеждает!")
        else:
            print("Бой завершился вничью.")

    @staticmethod
    def level_up_characters(hero_1, hero_2):
        if hero_1.hp > 0:
            hero_1.level_up()
            hero_1.reset_hp()
            print(f"{hero_1.name} повысил свой уровень до {hero_1.level}!")
        elif hero_2.hp > 0:
            hero_2.level_up()
            hero_2.reset_hp()
            print(f"{hero_2.name} повысил свой уровень до {hero_2.level}!")

    def start_game(self):
        hero_1 = self.select_character()
        hero_2 = characters[random.randint(0, 3)]
        print(f"Герой {hero_1.name} VS Герой {hero_2.name} ")
        while True:
            print(f"1) Start Fight\n"
                  f"2) View Info\n"
                  f"3) Exit Game")
            choose = int(input())
            match choose:
                case 1:
                    self.fight_hero(hero_1, hero_2)
                    self.level_up_characters(hero_1, hero_2)
                case 2:
                    print(f"Your Hero: ")
                    hero_1.display_options()
                    print("==================")
                    print("Your Enemy: ")
                    hero_2.display_options()
                case 3:
                    self.game_start()


if __name__ == "__main__":
    game = Game()
    game.game_start()


