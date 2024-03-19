# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             value = self.current
#             self.current += 1
#             return value
#
#
# my_iterator = MyIterator(1, 5)
#
# for num in my_iterator:
#     print(num)

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
#
#
# counter = count_up_to(5)
#
# for num in counter:
#     print(num)
#


# squares = (x**2 for x in range(1, 6))
#
# for num in squares:
#     print(num)
#

def even_odd_generator(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield f"{i} - Even"
        else:
            yield f"{i} - Odd"

# Створення генератора
my_generator = even_odd_generator(5)

# Використання функції next() для отримання наступного значення
print(next(my_generator))  # Виведе: 1 - Odd
print(next(my_generator))  # Виведе: 2 - Even
print(next(my_generator))  # Виведе: 3 - Odd



import time

# Генератор, що генерує послідовність чисел
def number_generator(n):
    for i in range(n):
        yield i

# Функція, яка обчислює суму послідовності чисел
def compute_sum(sequence):
    total = 0
    for num in sequence:
        total += num
    return total

# Вимірюємо час виконання з генератором
start_time = time.time()
my_generator = number_generator(1000000)
sum_with_generator = compute_sum(my_generator)
end_time = time.time()
execution_time_with_generator = end_time - start_time

# Вимірюємо час виконання зі списком
start_time = time.time()
my_list = list(range(1000000))
sum_with_list = compute_sum(my_list)
end_time = time.time()
execution_time_with_list = end_time - start_time

print("Час виконання з генератором:", execution_time_with_generator)
print("Час виконання зі списком:", execution_time_with_list)
print("Сума з генератором:", sum_with_generator)
print("Сума зі списком:", sum_with_list)
