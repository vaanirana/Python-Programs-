def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add functionality before calling the original function
        print("Something is happening before the function is called.")
        result = original_function(*args, **kwargs)
        # Add functionality after calling the original function
        print("Something is happening after the function is called.")
        return result
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()





def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
print("78.THIS PROGRAM IS WRITTEN BY DEEPANSHU, ERP:-005")THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
