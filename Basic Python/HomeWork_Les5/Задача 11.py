def dictator(dict_1, dict_2):
    res_dict = {}
    for key, value in dict_1.items():
        res_dict[key] = value

    for key, value in dict_2.items():
        res_dict[key] = res_dict.get(key, 0) + value
    print(res_dict)
    return res_dict


dictator({"Сухарики флинт": 1, "Мишаня Флинт": 2, "Артур": 3}, {"Жека Флинтовый": 4})
