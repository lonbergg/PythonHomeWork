
# Реверс через вайл
def my_reverse(pizdolist):
    dlina = len(pizdolist)
    my_list = []
    while dlina >= 1:
        my_list.append(pizdolist[-1])
        pizdolist.pop(-1)
        dlina -= 1
    return print(my_list)


def listed_map(func, iterable):
    try:
        spisochek = []
        for i in iterable:
            res = func(i)
            spisochek.append(res)
        return spisochek
    except TypeError:
        print('Нельзя применить функцию к елементам массива из-за неподходящего типа данных \n'
              'пошел нахуй!!!!!!!!')
        return iterable

    from math import sqrt

    piska = [1, 3, 5, 6, 5, 7, 5, 8, 3, 150]

    def my_reverse(pizdolist):
        spis = []
        end_of_list = len(pizdolist) - 1
        while end_of_list >= 0:
            spis.append(pizdolist[end_of_list])
            end_of_list -= 1
        return print(spis)

colors ={"green", "yellow", "red", "purple"}
colors.remove("red")
print(colors)



person = {"name": "Alisa", "age": 31, "city": "LA"}
person = dict(name = "Alisa", age = 31)
empty_dict = {}
