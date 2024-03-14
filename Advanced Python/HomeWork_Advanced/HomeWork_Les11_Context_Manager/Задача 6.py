import time


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            time.sleep(1.5)
        return cache[args]
    return wrapper


@memoize
def add(x, y):
    print("Посчитаем пачки сухариков в кеше ")
    return x + y


print(add(10, 12))
print(add(10, 12))
