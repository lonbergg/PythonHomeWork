# from contextlib import contextmanager
#
#
# @contextmanager
# def DividerContext(divider):
#     print(divider * 100)
#     yield
#     print(divider * 100)
#
#
# with DividerContext("*"):
#     print("This is inside the context.")

class DividerContext:

    def __init__(self, divider):
        self.divider = divider

    def __enter__(self):
        print(self.divider * 100)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.divider * 100)


with DividerContext("*"):
    print("Начало работы!")

