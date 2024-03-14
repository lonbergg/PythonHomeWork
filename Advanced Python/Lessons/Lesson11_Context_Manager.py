# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

# from contextlib import contextmanager
#
#
# @contextmanager
# def my_context():
#     # Виконання певних дій перед входом в контекст
#     print("Entering the context")
#
#     try:
#         # Виконання блоку коду в контексті
#         yield
#     finally:
#         # Виконання певних дій перед виходом з контексту
#         print("Exiting the context")
#
#
# with my_context():
#     # Блок коду, що виконується в контексті
#     print("Inside the context")
#
# class MyContext:
#     def __enter__(self):
#         # Виконання певних дій перед входом в контекст
#         print("Entering the context")
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         # Виконання певних дій перед виходом з контексту
#         print("Exiting the context")
#
# with MyContext():
#     # Блок коду, що виконується в контексті
#     print("Inside the context")
#
#
# class FileHandler:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file  # Повертаємо об'єкт файлу, що потрапляє до змінної після 'as'
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()
#
# # Використання контекстного менеджера
# with FileHandler('file.txt', 'r') as file:  # 'file' тут є об'єктом, повернутим __enter__()
#     content = file.read()
#     print(content)  # Друкуємо вміст файлу


def simple_decorator(function):
    def wrapper():
        print("Before function call")
        function()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()