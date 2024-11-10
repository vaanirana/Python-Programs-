#WAP to demonstrate Positional Parameters, Default Parameters, Keyword Parameters, Variable-Length Parameters
#Positional Parameters
def greet(name, age):
 print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30) # Output: Hello, Alice! You are 30 years old.
#Default Parameters
def greet(name, age=25):
 print(f"Hello, {name}! You are {age} years old.")
greet("Alice") # Output: Hello, Alice! You are 25 years old.
greet("Bob", 30) # Output: Hello, Bob! You are 30 years old.
#Keyword Parameters
def greet(name, age):
 print(f"Hello, {name}! You are {age} years old.")
greet(name="Alice", age=30) # Output: Hello, Alice! You are 30 years old.
greet(age=30, name="Alice") # Output: Hello, Alice! You are 30 years old.
#Variable-Length Parameters
#i)*args: For non-keyword variable-length arguments.
#*args collects all positional arguments into a tuple.
#The sum function calculates the sum of all elements in args.
def sum_numbers(*args):
 return sum(args)
print(sum_numbers(1, 2, 3)) # Output: 6
print(sum_numbers(4, 5, 6, 7, 8)) # Output: 30
#ii)**kwargs: For keyword variable-length arguments.
#**kwargs collects all keyword arguments into a dictionary.
#The function iterates through the dictionary and prints each key-value pair
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162")
