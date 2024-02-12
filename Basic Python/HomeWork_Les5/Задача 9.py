def spisochek():
    zapros = input("Введите числа через пробел: ")
    my_list = [int(х) for х in zapros.split()]
    double_spisok = [i * 2 for i in my_list]
    print(double_spisok)
spisochek()
