from contextlib import contextmanager
import time


@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Время выполнение {end_time - start_time}")


with timer():
    print("Начало работы")
    time.sleep(3)
    print("Завершение!")

# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end_time = time.time()
#         print(f"Время выполнения функции {self.end_time - self.start_time} секунл")
#
#
# with Timer():
#     print("Начало работы")
#     time.sleep(3)
#     print("Конец работы!")
