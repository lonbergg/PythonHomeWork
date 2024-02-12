year = int(input("Введите год для проверки на высокосность: "))

if year % 4 == 0:
    print("Yes")
elif year % 100 != 0:
    print("No")
elif year % 400 == 0:
    print("Yes")
