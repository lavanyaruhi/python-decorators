import time
import socket

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def send_message_to_server(server_address, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, port))
    s.sendall(message.encode('utf-8'))
    response = s.recv(1024)
    s.close()
    return response.decode('utf-8')

response = send_message_to_server("127.0.0.1", 555, "Hello, server!")
print(response)
