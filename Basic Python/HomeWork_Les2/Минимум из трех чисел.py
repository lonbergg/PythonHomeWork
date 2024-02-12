a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
e = int(input("Введите третье число: "))

if a < b and a < e:
    print(a)
elif b < a and b < e:
    print(b)
elif e < a and e < b:
    print(e)

