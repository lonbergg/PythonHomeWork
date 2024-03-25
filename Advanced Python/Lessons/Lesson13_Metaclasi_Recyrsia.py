# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# # Приклад виклику функції без рекурсії
# def fuctorial_non_rec(n):
#     result_without_recursion = 1
#     for i in range(1, n + 1):
#         result_without_recursion *= i
#     return result_without_recursion
#
#
# # Приклад виклику функції з рекурсією
# result_with_recursion = factorial(5)
#
# print("Результат без рекурсії:", fuctorial_non_rec(5))
# print("Результат з рекурсією:", result_with_recursion)
#
#
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#
#
#     def fibonacci(n):
#         if n <= 1:
#             return n
#         else:
#             return fibonacci(n - 1) + fibonacci(n - 2)
#
#     # Приклад виклику функції
#     result = fibonacci(7)
#     print("Результат обчислення числа Фібоначчі:", result)
#     # 13
#
#     prev, curr = 0, 1
#
#     for _ in range(2, n + 1):
#         prev, curr = curr, prev + curr
#
#     return curr
#
# # Приклад використання функції для обчислення 10-го числа Фібоначчі
# result = fibonacci(10)
# print(result)  # Виведе: 55

# class MyClass:
#     pass
#
# print(type(MyClass))  # <class 'type'>



# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         print('Creating class object')
#         return super().__new__(cls, name, bases, attrs)
#
#     def __init__(self, name, bases, attrs):
#         print('Initializing class object')
#         super().__init__(name, bases, attrs)
#
#
# class MyClass(metaclass=Meta):
#     pass
#
# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs["additional_attr"] = "Additional Attribute"
#         return super().__new__(cls, name, bases, attrs)
#
# class MyClass(metaclass=Meta):
#     pass
#
# my_instance = MyClass()
# print(my_instance.additional_attr)

# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         print("Пошел нахуй")
#         return super().__new__(cls, name, bases, attrs)
#
#     def __init__(self, name, bases, attrs):
#         print('Initializing class object')
#         super().__init__(name, bases, attrs)
#
#     class MyClass(metaclass=Meta):
#         pass

# class NameMeta(type):
#     def __init__(cls, name, bases, attrs):
#         if 'name' not in attrs:
#             raise TypeError("Class {} does not have a 'name' attribute.".format(name))
#         super().__init__(name, bases, attrs)
#
# class MyClass(metaclass=NameMeta):
#     name = 'MyClass'
#
# class MyOtherClass(metaclass=NameMeta):
#     pass  # will raise TypeError
