import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        return result
    return wrapper
@timer
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(calculate_sum(1000000))