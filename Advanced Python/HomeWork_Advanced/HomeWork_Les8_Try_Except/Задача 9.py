def del_line():

    file = open("file_1.txt", "w")
    file.write("Ебанные сухарики флинт пачка")
    file.close()

    file = open("file_1.txt", "r")
    content = file.read()
    print("То что находится в файле! ПРОЧИТАЙ!!!")
    print(content)
    file.close()

    line_delete_from_rydok = "флинт"
    file = open("file_1.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("file_1.txt", "w")
    for line in lines:
        if line.strip() != line_delete_from_rydok:
            file.write(line)
    file.close()

    file = open("file_1.txt", "r")
    content_after_delete = file.read()
    print("Вот что получилось!!!!")
    print(content_after_delete)
    file.close()

del_line()


