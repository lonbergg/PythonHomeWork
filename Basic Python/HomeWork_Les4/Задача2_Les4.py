word = input("Введите любое слов для проверки: ")
perevorot = word[::-1]

if word == perevorot:
    print(True)
else:
    print(False)
