import functools
import time

def retry(max_attempts, exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    res=func(*args, **kwargs)
                    return res
                except exception:
                    attempts += 1
                    print(f"Retrying {func.__name__}... Attempt {attempts}/{max_attempts}")
                    time.sleep(1)
            
            #raise exception(f"{func.__name__} failed after {max_attempts} attempts.")
            return None
        return wrapper
    return decorator
@retry(max_attempts=3, exception=ValueError)
def div(a, b):
    return a / b
    
try:
    result = div(10, 0)
    print("Result:", result)
except ValueError:
    print("Error: Cannot divide by zero.")
