# import random
#
# num = random.random()
# num_1 = random.randint(1,20)
# num_2 = random.uniform(1.0, 12.0)
#
# colors = ["красный", "синий", "желтый", "зеленый"]
# random_colors = random.choices(colors, k=3)
# color = random.choice(colors)
#
# num_3 = [1, 2, 3, 5, 6, 7, 8, 9, 20, 33, 55, 66]
# numbers_3 = random.sample(num_3,4)
#
# cards = ["A", "2", "3", "5", "B", "G"]
# random.shuffle(cards)
#
#
# number = random.randrange(1, 10, 2)
# print(number)
#
#
# dice_roll = random.randint(1, 6)  # Генерує число від 1 до 6
# print(f"Ви кинули {dice_roll}!")
#
# names = ["Анна", "Олександр", "Ірина", "Владислав"]
# chosen_one = random.choice(names)
# print(f"{chosen_one}, тобі доведеться виконати завдання!")
#
# print(num, num_1, num_2, color, numbers_3, cards, random_colors)
#
#
#
#
# import math
# res = math.sqrt(25)
# result = math.pow(3, 5)
# result_1 = math.floor(3.5)
# result_2 = math.ceil(3.2)
# result_3 = math.factorial(5)
# result_4 = math.log(15)
#
# radius = 5
# area = math.pi * math.pow(radius, 2)
# print(f"Площа кола з радіусом {radius} дорівнює {area}")
#
# number = 10
# factorial = math.factorial(number)
# print(f"Фак тебе {number}, сухарики фака {factorial}")
#
# print(res, result, result_1, result_2, result_3, result_4)
#
#
#
#
# import datetime
#
# # datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)
#
# # dt = datetime.datetime(2021, 9, 1)
#
# # dt = datetime.datetime(2021, 9, 1, 12, 30, 0)
# #
# # year = dt.year
# # month = dt.month
# # day = dt.day
# # hour = dt.hour
# # minute = dt.minute
# # second = dt.second
# # weekday = dt.weekday()
# # # Виводить певний формат дати
#
#
# dt = datetime.datetime(2024, 9, 1, 12, 33, 0)
#
# formatted_date = dt.strftime("%Y-%m-%d")
# formatted_time = dt.strftime("%H:%M:%S")
# formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
#
# print(formatted_date, formatted_time, formatted_datetime)
#
# current_datetime = datetime.datetime.now()
# print(current_datetime)
#
# from datetime import date
#
# today = date.today()
# formatted_date = today.strftime("%d/%m/%Y")
# print(f"Сьогоднішня дата: {formatted_date}")
#
# from datetime import date
#
# birth_date = date(1990, 5, 12)
# today = date.today()
# age = today.year - birth_date.year
# if (today.month, today.day) < (birth_date.month, birth_date.day):
#     age -= 1
# print(f"Вам {age} років.")


import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

#
# txt = "Дощ у Іспанії"
# x = re.findall("і", txt)
# print(x)
import re
txt = "Дощ у Іспанії"
x = re.search(r"\s", txt)

print("Перший символ пробілу розташований на позиції:", x.start())

txt = "Дощ у Іспанії"
x = re.search("Португалія", txt)
print(x)

import re

txt = "Дощ у Іспанії"
x = re.split(r"\s", txt)
print(x)

txt = "Дощ у Іспанії"
x = re.search("і", txt)
print(x) # це виведе об'єкт

txt = "Дощ у Іспанії"
x = re.search(r"\bІ\w+", txt)
print(x.span())

email = 'example@example.com'
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Email валідний.")
else:
    print("Email не валідний.")