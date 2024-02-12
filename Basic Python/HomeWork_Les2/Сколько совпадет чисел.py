first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число "))

if first_number == second_number == third_number:
    print("Все три числа cовпадают ")
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print("Два числа совпадают! ")
else:
    print("Все числа различны!")
