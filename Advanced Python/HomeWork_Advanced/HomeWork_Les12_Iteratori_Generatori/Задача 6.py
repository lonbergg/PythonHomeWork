def odd_number_filter(n):
    for i in n:
        if i % 2 != 0:
            yield f"{i} - Непарные"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = odd_number_filter(numbers)
for num in odd_nums:
    print(num)
