def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    print(res)


factorial(3)