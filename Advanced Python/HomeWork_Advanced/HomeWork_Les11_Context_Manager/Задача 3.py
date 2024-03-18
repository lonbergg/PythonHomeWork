def log_func(function):
    def wrapper():
        print("Здарова бандиты функция начала работу")
        function()
        print("Покеда бандиты конец работы!")
    return wrapper


@log_func
def say_bye():
    print("Пошел назуй!")


say_bye()
