def authenticate(func):
    def wrapper(*args, **kwargs):
        password = input("Enter the password: ")
        if password == "secret":
            return func(*args, **kwargs)
        else:
            print("Authentication failed. Access denied.")
    return wrapper
@authenticate
def secure_function():
    print("Access granted. This is a secure function.")

secure_function()
