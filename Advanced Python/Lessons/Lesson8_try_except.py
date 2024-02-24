# try:
#     # Код, в якому може виникнути помилка
#     x = 10 / 0  # Ділення на нуль
# except ZeroDivisionError:
#     # Код для обробки помилки
#     print("Помилка: Ділення на нуль!")

# try:
#     num_1 = int(input("Введите первое число: "))
#     num_2 = int(input("Введите второе число: "))
#     result = num_1 / num_2
#     print("Результат сухариков", result)
# except ZeroDivisionError:
#     print("Ошибка! Пошел нахуй! подели на ноль свое очко!")
# except ValueError:
#     print("Некоректно ввел число еблоид пошел нахуй!!!!")

try:

    result = 10 / 2
except ZeroDivisionError:
    print("Помилка: Ділення на нуль!")
else:
    print("Результат: ", result)
finally:
    print("Завершення обробки")


try:
    numerator = int(input("Введіть чисельник: "))
    denominator = int(input("Введіть знаменник: "))
    result = numerator / denominator
    print("Результат:", result)
except ZeroDivisionError:
    print("Помилка: Ділення на нуль!")


try:
    age = int(input("Введіть ваш вік: "))
    if age < 0:
        raise ValueError("Некоректне значення: вік не може бути від'ємним")
    print("Ваш вік:", age)
except ValueError as e:
    print("Помилка:", str(e))


try:
    file = open("несуществующий_файл.txt", "r")
    content = file.read()
    file.close()
    print("Вміст файлу:", content)
except FileNotFoundError:
    print("Помилка: Файл не знайдено")

    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Спроба доступу до неіснуючого індексу
    except IndexError:
        print("Помилка: Неправильний індекс списку")


try:
    number = int(input("Введіть число: "))
except ValueError:
    print("Помилка: Некоректне число")
else:
    result = number * 2
    print("Результат:", result)
finally:
    print("Завершення обробки")


try:
    # Код, який може викликати виняток
    ...
except Exception as e:
    # Обробка винятку
    ...