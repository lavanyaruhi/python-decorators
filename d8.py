import functools
def handle_network_exceptions(default_response):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except (ConnectionError, TimeoutError) as e:
                # Handle specific network-related exceptions here
                # You can implement various actions like retrying, logging, or returning a default response
                print(f"Network exception occurred: {str(e)}")
                print("Retrying request...")
                # Retry the request
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                # Handle other exceptions here
                print(f"Unhandled exception occurred: {str(e)}")
                # Return a default response or raise the exception
                return default_response
        return wrapper

    return decorator

# Example usage
@handle_network_exceptions("Default Response")
def make_network_request(url):
    # Simulating a network-related exception
    raise ConnectionError("Connection failed")

response = make_network_request("https://api.example.com")
print(response)
