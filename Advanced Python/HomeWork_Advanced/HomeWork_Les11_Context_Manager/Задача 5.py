def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def function(count):
    print(f"Cколько у тебя пачек сухариков флинт? СТОЛЬКО НАХУЙ {count}")


function(20)
