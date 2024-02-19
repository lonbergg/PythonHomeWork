def delitel():
    try:
        num_1 = int(input("Введите коректное число: "))
        num_2 = int(input("Введите второе корректное число: "))
        result = num_1 / num_2
        print(result, "Вы не далбоеб и знаете много!!!! ")
    except ZeroDivisionError:
        print("Вы далбоеб! Делить на ноль нельзя!")
    except ValueError:
        print("Введены некорректные числа!!ТУПОЙ!!")


delitel()