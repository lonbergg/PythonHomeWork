def spisocheck(my_list):
    result_list = []
    for i in my_list:
        if i % 2 == 0:
            result_list.append(i)
    return print(result_list)


spisocheck([1, 2, 2, 4, 4, 5, 5, 6, 6, 4, 7, 8, 8, 9, 11])
