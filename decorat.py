def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished execution")
        return result
    return wrapper
    
def logs(fun):
    def wrapper(*args, **kwargs):
        print(f"Exception function {fun.__name__}")
        result = fun(*args, **kwargs)
        print(f"Function {fun.__name__} finished execution")
        return result
    return wrapper

@log_execution
#@logs
def add_numbers(x, y):
    return x + y
print(add_numbers(2, 8))  