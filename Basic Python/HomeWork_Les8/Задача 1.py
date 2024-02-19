def check():
    try:
        my_list = [1, 2, 3, 4, 5]
        print(my_list[7])
    except IndexError:
        print("Ты ебло это ОШИБКА! Инедкса такого нету!!!!!")
check()