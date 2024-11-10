# SWAPPING VALUES OF TWO VARIABLES USING TEMPORARY VARIABLE
a = input("enter the value of a:")
b = input("enter the value of b:")
# swapping using temporary var
temp = a
a = b
b = temp
print(f"After swapping (method 1): a = {a}, b = {b} ")

#without using temoporary variable
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
# swapping using none temporary var
a = a + b
b = a - b
a = a - b
print(f"After swapping (method 2): a = {a}, b = {b} ")

# using tuple
a = input("enter the value of a:")
b = input("enter the value of b:")
# swapping using tuple
a, b = b, a
print(f"After swapping (method 3): a = {a}, b = {b} ")
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:- 162")

