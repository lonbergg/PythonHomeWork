import time


def timeit(function):
    def wrapper():
        print("Начало работы функции! Подожди бля!")
        time.sleep(2)
        function()
        print("Конец работы функции! Пока бля! Надо опять ждать! Прикинь бля")
        time.sleep(1.5)
        function()

    return wrapper


@timeit
def time_check():
    start_time = time.time()
    end_time = time.time()
    print(f"Время выполнения функции {end_time - start_time} секунд")


time_check()
