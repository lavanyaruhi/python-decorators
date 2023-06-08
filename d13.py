def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log
def multiply(a, b):
    return a * b

result = multiply(5, 7)
print(result)
