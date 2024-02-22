def input_str():
    vvod_slova = input("Введите любое слово или хуй знает шо: ")

    file = open("file.txt", "w")
    file.write("Навалил кринжа = ")
    file.close()

    file = open("file.txt", "a")
    file.write(vvod_slova)
    file.close()

    file = open("file.txt", "r")
    content = file.read()
    print("Cтрока успешна записана в файл!")
    print(content)


input_str()