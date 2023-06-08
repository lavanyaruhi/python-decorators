import functools

def retry(exception, retries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    result = func(*args, **kwargs)
                except exception:
                    print(f"Retrying {func.__name__}...")
                else:
                    return result
            return None  # Or raise an exception if all retries failed
        return wrapper
    return decorator

@retry(ValueError, retries=5)
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
