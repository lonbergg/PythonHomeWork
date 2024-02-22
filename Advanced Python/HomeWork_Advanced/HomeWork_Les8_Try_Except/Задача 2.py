def numbers():
    try:
        num_1 = int(input("Введиье первое число: "))
        num_2 = int(input("Введите второе число: "))
        result = num_1 + num_2
        print("Ты ввел нормальные числа! ТЕБЕ СУХАРИКИ ФЛИНТ МЕГАПАЧКУ ЗА МОЙ СЧЕТ!", result)
    except ValueError:
        print("Введи чилос еблоид, а не стр!!!!!")


numbers()