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


# import random
# from enum import Enum
# import sys
# import time
#
#
# class CharacterType(Enum):
#     WARRIOR = 0
#     ARCHER = 1
#     WIZARD = 2
#     RIDER = 3
#
#
# class Faction(Enum):
#     WHITE = 0
#     RED = 1
#     BLUE = 2
#
#
# class Character:
#     def __init__(self, name, hp, damage, critical_damage, luck, level, faction):
#         self.name = name
#         self.hp = hp
#         self.current_hp = hp
#         self.damage = damage
#         self.critical_damage = critical_damage
#         self.luck = luck
#         self.level = level
#         self.faction = faction
#
#     def display_options(self):
#         return print(f"Характеристика героя \n"
#                      f"Hero: {self.name}\n"
#                      f"Уровень здоровья HP = {self.current_hp}\n"
#                      f"Базовый Урон Damage = {self.damage}\n"
#                      f"Критический Урон Critical Damage = {self.critical_damage}\n"
#                      f"Удача Luck = {self.luck}\n"
#                      f"Уровень Level = {self.level}\n"
#                      f"Фракция Faction = {self.faction}\n")
#
#     def dmg(self):
#         lucky = random.randint(1, 100)
#         if lucky <= self.luck:
#             crit = self.damage + (self.damage * self.critical_damage)
#             print(f'----- {crit} CRITICAL DAMAGE -----')
#             return crit
#         else:
#             return self.damage
#
#     def level_up(self):
#         self.level += 1
#         self.current_hp = self.get_health() + (self.get_health() * (0.15 * (self.level - 1)))
#         self.damage += 5
#         self.critical_damage += 0.10
#         self.luck += 3
#
#     def get_health(self):
#         return self.hp
#
#     def heal(self):
#         self.current_hp = self.get_health()
#         self.level = 1
#
#
# class Warrior(Character):
#     def __init__(self, faction=Faction.WHITE):
#         super().__init__("Warrior", 150, 20, 0.3, 10, 1, faction)
#
#     def attack(self, enemy):
#         if isinstance(enemy, Wizard):
#             if enemy.faction == Faction.RED:
#                 return self.dmg() + (self.damage * 0.15) + (self.damage * 0.05)
#         return self.dmg()
#
#
# class Archer(Character):
#     def __init__(self, faction=Faction.BLUE):
#         super().__init__("Archer", 140, 18, 0.35, 20, 1, faction)
#
#     def attack(self, enemy):
#         if isinstance(enemy, Rider):
#             if enemy.faction == Faction.WHITE:
#                 return self.dmg() + (self.damage * 0.15) + (self.damage * 0.05)
#         return self.dmg()
#
#
# class Wizard(Character):
#     def __init__(self, faction=Faction.RED):
#         super().__init__("Wizard", 130, 25, 0.40, 15, 1, faction)
#
#     def attack(self, enemy):
#         if isinstance(enemy, Archer):
#             if enemy.faction == Faction.BLUE:
#                 return self.dmg() + (self.damage * 0.15) + (self.damage * 0.05)
#         return self.dmg()
#
#
# class Rider(Character):
#     def __init__(self, faction=Faction.BLUE):
#         super().__init__("Rider", 160, 22, 0.25, 12, 1, faction)
#
#     def attack(self, enemy):
#         if isinstance(enemy, Warrior):
#             if enemy.faction == Faction.WHITE:
#                 return self.dmg() + (self.damage * 0.15) + (self.damage * 0.05)
#         return self.dmg()
#
#
# def char(char_type: CharacterType, faction=Faction.WHITE):
#     char_dict = {
#         CharacterType.WARRIOR: Warrior,
#         CharacterType.ARCHER: Archer,
#         CharacterType.WIZARD: Wizard,
#         CharacterType.RIDER: Rider
#     }
#     return char_dict[char_type](faction)
#
#
# characters = [char(CharacterType.WARRIOR, Faction.WHITE),
#               char(CharacterType.ARCHER, Faction.BLUE),
#               char(CharacterType.WIZARD, Faction.RED),
#               char(CharacterType.RIDER, Faction.BLUE)]
#
#
# class Game:
#     def __init__(self):
#         self.army_types = {Faction.WHITE: "Белые", Faction.RED: "Красные", Faction.BLUE: "Синие"}
#
#     def game_start(self):
#         while True:
#             print("1. Начать игру / Битва Героев 1 vs 1 ")
#             print("2. Начать игру / Битва Армий ")
#             print("3. Информация про Героев")
#             print("4. Покинуть игру")
#             choose = int(input("Введите число от 1-4 чтобы выбрать действие: "))
#             match choose:
#                 case 1:
#                     self.start_game()
#                 case 2:
#                     self.battle_army()
#                 case 3:
#                     print("Информация про Героев:\n")
#                     for character_type in CharacterType:
#                         for faction in Faction:
#                             hero = char(character_type, faction)
#                             time.sleep(1)
#                             print(f"Тип Героя: {hero.name}, Фракция: {self.army_types[faction]}")
#                             hero.display_options()
#                             print("=====================")
#                 case 4:
#                     print(f"Береги себя, путник! До новых встреч! Прощай!")
#                     sys.exit()
#                 case _:
#                     print("Incorrect input, please try again")
#                     self.game_start()
#
#     @staticmethod
#     def select_character(faction=Faction.WHITE):
#         print("| Выберите своего игрового персонажа          |")
#         print("| Введите 1 для выбора =====> Warrior(Воин)   |")
#         print("| Введите 2 для выбора =====> Archer(Лучник)  |")
#         print("| Введите 3 для выбора =====> Wizard(Маг)     |")
#         print("| Введите 4 для выбора =====> Rider(Наездник) |")
#
#         choose = int(input("Введите число от 1-4 чтобы выбрать действие: "))
#         match choose:
#             case 1:
#                 choose = characters[0]
#             case 2:
#                 choose = characters[1]
#             case 3:
#                 choose = characters[2]
#             case 4:
#                 choose = characters[3]
#             case _:
#                 print("Некоректный выбор! Персонаж не выбран! Попробуй снова!")
#         return choose
#
#     @staticmethod
#     def fight_hero(hero_1, hero_2):
#         print(f"Битва {hero_1.name} vs {hero_2.name} Valhalla Coming For YOU BITCH! ")
#         print(f"Fight!\n")
#         while True:
#             print(f"{hero_1.name} сражается с {hero_2.name}!")
#             damage_dealt = hero_1.attack(hero_2)
#             hero_2.current_hp -= damage_dealt
#             print(f"{hero_1.name} наносит {damage_dealt} урона.")
#             print('<--------------------------------------------->')
#             time.sleep(2)
#             if hero_2.current_hp <= 0:
#                 print(f"{hero_2.name} погибает. {hero_1.name} побеждает!")
#                 return
#
#             print(f"{hero_2.name} сражается с {hero_1.name}!")
#             damage_dealt = hero_2.attack(hero_1)
#             hero_1.current_hp -= damage_dealt
#             print(f"{hero_2.name} наносит {damage_dealt} урона.")
#             print('<--------------------------------------------->')
#             time.sleep(2)
#             if hero_1.current_hp <= 0:
#                 print(f"{hero_1.name} погибает. {hero_2.name} побеждает!")
#                 return
#
#             print(f"\nТекущее здоровье {hero_1.name}: {hero_1.current_hp}")
#             print(f"Текущее здоровье {hero_2.name}: {hero_2.current_hp}\n")
#
#     @staticmethod
#     def level_up_characters(hero_1, hero_2):
#         if hero_1.current_hp <= 0:
#             hero_2.level_up()
#             hero_1.heal()
#             print(f"{hero_2.name} Win! {hero_1.name} Lose!")
#             print(f"{hero_2.name} повысил свой уровень до {hero_2.level}!")
#             print(f"{hero_1.name} остался на прежнем уровне!")
#             return True
#         elif hero_2.current_hp <= 0:
#             hero_1.level_up()
#             hero_2.heal()
#             print(f"{hero_1.name} Win! {hero_2.name} Lose!")
#             print(f"{hero_1.name} повысил свой уровень до {hero_1.level}!")
#             print(f"{hero_2.name} остался на прежнем уровне!")
#             return True
#         return False
#
#     @staticmethod
#     def army_stats(army):
#         total_health = sum(hero.current_hp for hero in army)
#         total_damage = sum(hero.damage for hero in army)
#         average_level = sum(hero.level for hero in army) / len(army)
#         most_popular_unit = max(set(hero.name for hero in army), key=army.count)
#         return total_health, total_damage, average_level, most_popular_unit
#
#     def assemble_army(self, army_size, faction=Faction.WHITE):
#         army = []
#         print(f"Сбор армии ({self.army_types[faction]}):")
#         for i in range(army_size):
#             hero = self.select_character(faction)
#             army.append(hero)
#             print(f"Герой {hero.name} добавлен в армию.")
#         return army
#
#     @staticmethod
#     def battle_army():
#         game = Game()
#         print("Сбор армии 1:")
#         army_1_size = int(input("Введите размер армии 1: "))
#         army_1_faction = Faction(int(input("Введите фракцию армии 1 (0 - WHITE, 1 - RED, 2 - BLUE): ")))
#         army_1 = game.assemble_army(army_1_size, army_1_faction)
#
#         print("\nСбор армии 2:")
#         army_2_size = int(input("Введите размер армии 2: "))
#         army_2_faction = Faction(int(input("Введите фракцию армии 2 (0 - WHITE, 1 - RED, 2 - BLUE): ")))
#         army_2 = game.assemble_army(army_2_size, army_2_faction)
#
#         print("Битва Армий начинается!\n")
#
#         army_1_health, army_1_damage, army_1_avg_level, army_1_most_popular = game.army_stats(army_1)
#         army_2_health, army_2_damage, army_2_avg_level, army_2_most_popular = game.army_stats(army_2)
#
#         print(f"Армия 1 ({game.army_types[army_1_faction]}) (Общее здоровье: {army_1_health}, "
#               f"Общий урон: {army_1_damage}, Средний уровень: {army_1_avg_level}, "
#               f"Самый популярный тип юнита: {army_1_most_popular})")
#         print(f"Армия 2 ({game.army_types[army_2_faction]}) (Общее здоровье: {army_2_health}, "
#               f"Общий урон: {army_2_damage}, Средний уровень: {army_2_avg_level}, "
#               f"Самый популярный тип юнита: {army_2_most_popular})")
#         print("===========================================================")
#
#         while army_1_health > 0 and army_2_health > 0:
#             army_2_health -= army_1_damage
#             print(f"ARMY 1 наносит {army_1_damage} урона армии 2.")
#             army_1_health -= army_2_damage
#             print(f"ARMY 2 наносит {army_2_damage} урона армии 1.\n")
#             print(f"Общее здоровье ARMY 1: {army_1_health} HP\n"
#                   f"Общее здоровье ARMY 2: {army_2_health} HP")
#             print('<--------------------------------------------->')
#             time.sleep(2)
#
#         if army_1_health <= 0:
#             print(f"ПОБЕДИЛА АРМИЯ 2 ({game.army_types[army_2_faction]}")")
#         else:
#             print(f"ПОБЕДИЛА АРМИЯ 1 ({game.army_types[army_1_faction]}")")
#
#     def start_game(self):
#         game = Game()
#         hero_1_faction = Faction(int(input("Введите фракцию вашего персонажа (0 - WHITE, 1 - RED, 2 - BLUE): ")))
#         hero_1 = self.select_character(hero_1_faction)
#         hero_2 = characters[random.randint(0, 3)]
#         print(f"Герой {hero_1.name} ({game.army_types[hero_1_faction]}) VS Герой {hero_2.name} ({game.army_types[hero_2.faction]})")
#         while True:
#             print(f"1) Start Fight\n"
#                   f"2) View Info\n"
#                   f"3) Выход в меню для выбора нового Героя")
#             choose = int(input())
#             match choose:
#                 case 1:
#                     self.fight_hero(hero_1, hero_2)
#                     if self.level_up_characters(hero_1, hero_2):
#                         return
#                 case 2:
#                     print(f"Your Hero: ")
#                     hero_1.display_options()
#                     print("==================")
#                     print("Your Enemy: ")
#                     hero_2.display_options()
#                 case 3:
#                     self.game_start()
#
#
# if __name__ == "__main__":
#     game = Game()
#     game.game_start()

