import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        elapsedTime = end_time - start_time
        print(f"Elapsed time: {elapsedTime} seconds")
        return res
    return wrapper
@timer
def compute_sum(n):
    return sum(range(n))
print(compute_sum(1000000))
