import random
from enum import Enum


class CharacterType(Enum):
    Warrior = 1
    Archer = 2
    Wizard = 3
    Rider = 4


class Character:
    def __init__(self, hp, damage, critical_damage, luck):
        self.hp = hp
        self.damage = damage
        self.critical_damage = critical_damage
        self.luck = luck

    def display_options(self):
        return print(f"    Характеристика героя \n"
                     f"Уровень здоровья HP = {self.hp}\n"
                     f"Базовый Урон Damage = {self.damage}\n"
                     f"Критический Урон Critical Damage = {self.critical_damage}\n"
                     f"Удача Luck = {self.luck}\n")


class Warrior(Character):
    def __init__(self):
        super().__init__(150, 20, 30, 10)

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage + self.critical_damage)
            return crit
        else:
            return self.damage


class Archer(Character):
    def __init__(self):
        super().__init__(140, 18, 35, 20)

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage + self.critical_damage)
            return crit
        else:
            return self.damage


class Wizard(Character):
    def __init__(self, ):
        super().__init__(130, 25, 40, 15)

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage + self.critical_damage)
            return crit
        else:
            return self.damage


class Rider(Character):
    def __init__(self, ):
        super().__init__(160, 22, 25, 12)

    def dmg(self):
        lucky = random.randint(1, 100)
        if lucky <= self.luck:
            crit = self.damage + (self.damage + self.critical_damage)
            return crit
        else:
            return self.damage


class Game:

    @staticmethod
    def game_start():
        while True:
            try:
                print("1. Начать игру")
                print("2. Узнать характеристики героев")
                print("3. Покинуть игру")
                choose = int(input("Введите число от 1-3 чтобы выбрать действие: "))
                if choose not in [1, 2, 3]:
                    raise ValueError("Некорректный ввод числа, попробуйте снова!")
                return choose
            except ValueError as e:
                print(e)

    @staticmethod
    def select_character(characters):
        print("| Выберите своего игрового персонажа          |")
        print("| Введите 1 для выбора =====> Warrior(Воин)   |")
        print("| Введите 2 для выбора =====> Archer(Лучник)  |")
        print("| Введите 3 для выбора =====> Wizard(Маг)     |")
        print("| Введите 4 для выбора =====> Rider(Наездник) |")

        choose = int(input("Введите число от 1-4 чтобы выбрать действие: "))
        match choose:
            case 1:
                selected_character = characters[0]
            case 2:
                selected_character = characters[1]
            case 3:
                selected_character = characters[2]
            case 4:
                selected_character = characters[3]
            case _:
                print("Некоректный выбор! Персонаж не выбран! Попробуй снова!")
                return None

        selected_character.display_options()
        return selected_character

    @staticmethod
    def display_stats_hero(character_type):
        selected_character = char(character_type)
        selected_character.display_options()
        return character_type


def char(char_type: CharacterType):
    char_dict = {
        CharacterType.Warrior: Warrior,
        CharacterType.Archer: Archer,
        CharacterType.Wizard: Wizard,
        CharacterType.Rider: Rider
    }
    return char_dict[char_type]()


characters = [char(CharacterType.Warrior),
              char(CharacterType.Archer),
              char(CharacterType.Wizard),
              char(CharacterType.Rider)]

if __name__ == "__main__":
    game = Game()
    game.game_start()
