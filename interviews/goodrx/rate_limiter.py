import time
from functools import wraps
from collections import deque


def rate_limited(max_calls_per_minute):
    """
    """
    min_interval = 60.0 / max_calls_per_minute
    call_times = deque()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import ipdb; ipdb.set_trace()
            current_time = time.time()

            while call_times and current_time - call_times[0] > min_interval:
                call_times.popleft()

            if len(call_times) < max_calls_per_minute:
                result = func(*args, **kwargs)
                call_times.append(current_time)
                return result
            else:
                sleep_time = min_interval - (current_time - call_times[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                result = func(*args, **kwargs)
                call_times.append(current_time)
                return result

        return wrapper

    return decorator


@rate_limited(1)
def my_function():
    print("Function executed")


if __name__ == "__main__":
    for _ in range(10):
        my_function()
