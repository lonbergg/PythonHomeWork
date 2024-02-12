def my_list(str):
    words = str.split()
    new_word = [word.capitalize() for word in words]
    new_rydok = " ".join(new_word)
    return print(new_rydok)


my_list("Артур пошел ты в сухарики флинт")
