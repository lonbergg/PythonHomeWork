def work_file():
    file = open("file.txt", "w")
    file.write("Текст сухариков флинт мега пачка со вкусом краба")
    file.close()

    file = open("file.txt", "r")
    content = file.read()
    words = content.split()
    chislo = len(words)
    print(chislo)
    file.close()


work_file()