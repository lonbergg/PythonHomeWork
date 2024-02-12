def ryadok(sentence):
    new_dict = {}
    for word in sentence.split():
        new_dict[word] = len(word)
    return print(new_dict)


ryadok("Жека как тебе сухарики флинт?")
