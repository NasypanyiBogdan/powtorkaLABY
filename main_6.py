import time
from functools import wraps

def time_limit_logger(limit_seconds=1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time

            if duration > limit_seconds:
                print(f"Увага: функція '{func.__name__}' виконувалась {duration:.2f} секунд(и), що перевищує ліміт {limit_seconds} секунд.")
            return result
        return wrapper
    return decorator

@time_limit_logger(limit_seconds=1.0)
def long_running_task():
    print("Початок довгої задачі...")
    time.sleep(1.5)
    print("Кінець задачі.")

long_running_task()
