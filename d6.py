import time
import functools

def rate_limit(limit_per_second):
    def decorator(func):
        last_call_time = 0
        calls_made = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call_time, calls_made

            # Calculate the time elapsed since the last call
            elapsed_time = time.time() - last_call_time

            if elapsed_time < 1:
                # If the elapsed time is less than 1 second, check the number of calls made
                if calls_made >= limit_per_second:
                    # Limit exceeded, do not execute the function
                    print(f"Rate limit exceeded. Limiting to {limit_per_second} calls per second.")
                    return None  # or raise an exception, redirect, etc.

            # Reset the counter if the elapsed time is greater than or equal to 1 second
            if elapsed_time >= 1:
                calls_made = 0

            # Update the last call time and increment the calls made counter
            last_call_time = time.time()
            calls_made += 1

            # Execute the function
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

# Example usage
@rate_limit(1)  # Allowing 2 calls per second
def make_network_request(url):
    print(f"Making network request to {url}")

# Simulated network requests
make_network_request("https://api.example.com")
make_network_request("https://api.example.com")
make_network_request("https://api.example.com")  # Rate limit exceeded
