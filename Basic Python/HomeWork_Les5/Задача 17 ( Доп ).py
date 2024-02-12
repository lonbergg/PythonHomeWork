# def arguments (first, second):
#     my_list_1 = []
#     my_list_2 = []
#     for i in first:
#         if i % 2 == 0:
#             my_list_1.append(i)
#         elif i % 2 != 0:
#             my_list_2.append(i)
#
#     for i in second:
#         if i % 2 == 0:
#             my_list_1.append(i)
#         elif i % 2 != 0:
#             my_list_2.append(i)
#     print(f"Список четных чисел: {my_list_1}, Список сухариков флинт с крабом {my_list_2}")
#
# arguments([2, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], [18, 19, 20, 21, 22, 23, 24, 26])


def check(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


def my_filter(function, iterable):
    my_list = []
    for i in iterable:
        res = function(i)
        if res is True:
            my_list.append(i)
    return print(my_list)


my_list_1 = [2, 3, 44, 12, 33, 22, 31]
print(tuple(filter(check, my_list_1)))
