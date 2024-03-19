def even_odd_generator(n):
    for num in range(1, n):
        if num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        elif num % 3 == 0:
            yield "Fizz"
        elif num % 5 == 0:
            yield "Buzz"
        else:
            yield num


for el in even_odd_generator(16):
    print(el)
