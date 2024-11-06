def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper  # Return the wrapper function

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Call the decorated function
THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
