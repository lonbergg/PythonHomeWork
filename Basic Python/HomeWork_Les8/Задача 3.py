def proverka():
    try:
        file = open('file.txt', 'r')
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("Такого файла не сущесвтует")


proverka()