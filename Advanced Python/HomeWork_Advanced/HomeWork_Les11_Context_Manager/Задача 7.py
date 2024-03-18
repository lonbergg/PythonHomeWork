import time
from datetime import datetime, timedelta


def rate_limit(calls, period):
    times = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal times
            now_time = datetime.now()
            times[:] = [time for time in times if time < now_time + timedelta(seconds=period)]
            if len(times) < calls:
                times.append(now_time)
                return func(*args, **kwargs)
            else:
                print("Try again!")

        return wrapper
    return decorator


@rate_limit(5, 10)
def greet():
    time.sleep(1)
    return print("Fuck you!")


for _ in range(7):
    greet()
