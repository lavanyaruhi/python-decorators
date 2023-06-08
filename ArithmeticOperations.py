def arithmetic_operation(func):
    def wrap(x, y):
        print("Performing arithmetic operation...")
        print(f"{func.__name__}",end=" ")
        result = func(x, y)
        print("Result:", result)
        return result
    return wrap

@arithmetic_operation
def add(x, y):
    return x + y

@arithmetic_operation
def subtract(x, y):
    return x - y

@arithmetic_operation
def multiply(x, y):
    return x * y

@arithmetic_operation
def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero!")
        return None

# Testing the arithmetic operations
add(5, 3)
subtract(10, 7)
multiply(4, 6)
divide(8, 2)
divide(10, 0)
