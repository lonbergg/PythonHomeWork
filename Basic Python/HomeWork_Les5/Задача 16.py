def count_vowels(*args):
    vowels = "ауоиэыяюеё"
    result_dict = {}

    for word in args:
        for char in word:
            if char.lower() in vowels:
                result_dict[char.lower()] = result_dict.get(char.lower(), 0) + 1

    return print(result_dict)


count_vowels("Мишаня любит сухарики", "Жека не любит майонез!")
