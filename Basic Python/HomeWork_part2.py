def my_filter(function, iterable):
    new_list = []
    for i in iterable:
        if function(i) is True:
            new_list.append(i)
    return new_list