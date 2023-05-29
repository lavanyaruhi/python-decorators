import functools
import time

def cache_response(duration):
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))

            if key in cache:
                cached_time, response = cache[key]
                current_time = time.time()

                if current_time - cached_time <= duration:
                    print("Retrieving response from cache.")
                    return response

            response = func(*args, **kwargs)
            cache[key] = (time.time(), response)

            return response

        return wrapper

    return decorator

# Example usage
@cache_response(60)  # Cache the response for 60 seconds
def make_network_request(url):
    print(f"Making network request to {url}")
    # Simulating network request delay
    time.sleep(2)
    return f"Response from {url}"

# First call triggers a network request
response1 = make_network_request("https://api.example.com")
print(response1)

# Subsequent call within the cache duration retrieves the response from cache
response2 = make_network_request("https://api.example.com")
print(response2)

# Wait for cache duration to expire
time.sleep(60)

# Call after cache duration expires triggers a new network request
response3 = make_network_request("https://api.example.com")
print(response3)
