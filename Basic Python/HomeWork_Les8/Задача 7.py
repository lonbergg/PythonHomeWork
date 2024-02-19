def file_work():

    file = open("file.txt", "w")
    file.write("Сухарики = ")
    file.close()

    file = open("file_2.txt", "w")
    file.write("ФЛИНТ со вкусом ебейшего краба")
    file.close()

    file = open("file.txt", "r")
    content = file.read()
    file.close()

    file = open("file_2.txt", "w")
    file.write(content)
    file.close()

    file = open("file_2.txt", "r")
    baza = file.read()
    print(baza)
    file.close()


file_work()
