import functools
import requests

def log_request_details(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        
        # Extract request details
        request_method = response.request.method
        request_url = response.request.url
        request_headers = response.request.headers
        response_status = response.status_code
        
        # Log request details
        print(f"Request Method: {request_method}")
        print(f"Request URL: {request_url}")
        print(f"Request Headers: {request_headers}")
        print(f"Response Status: {response_status}")
        
        return response
    
    return wrapper

# Example usage
@log_request_details
def make_network_request(url):
    response = requests.get(url)
    return response

response = make_network_request("https://www.google.com")
print(response.content)
