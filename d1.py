import logging

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

# Configure logging
logging.basicConfig(level=logging.INFO)

# Call the decorated function
result = add_numbers(3, 5)
print(result)  #8
