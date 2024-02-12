def vowels(sentence):
    res = 0
    vowels = "ауоиэыяюеё"
    for char in sentence:
        if char in vowels:
            res += 1
    return print(res)


vowels("Мишаня здарова сухарики флинт хочешь?")
