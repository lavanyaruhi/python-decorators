import time
import requests

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        #print(result)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

@measure_execution_time
def make_network_request(url):
    response = requests.get(url)
    return response.status_code

result = make_network_request("https://www.google.com")
print(result)  # Output: HTTP status code of the response

