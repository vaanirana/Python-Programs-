q35. Write a python code to print first n armstrong number that comes after the given number x

def is_armstrong(number):
    # Convert the number to a string to iterate over digits
    digits = str(number)
    # Find the number of digits
    num_digits = len(digits)
    # Calculate the sum of the digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    # Check if the sum is equal to the original number
    return armstrong_sum == number

def find_armstrong_after_x(x, n):
    armstrong_numbers = []
    current_number = x + 1
    
    # Continue finding Armstrong numbers until we have found n of them
    while len(armstrong_numbers) < n:
        if is_armstrong(current_number):
            armstrong_numbers.append(current_number)
        current_number += 1
    
    return armstrong_numbers

# Input x and n from the user
x = int(input("Enter the number after which to find Armstrong numbers: "))
n = int(input("Enter the number of Armstrong numbers to find: "))

# Find the first n Armstrong numbers after x
armstrong_numbers = find_armstrong_after_x(x, n)

# Print the Armstrong numbers
print(f"The first {n} Armstrong numbers after {x} are:", armstrong_numbers)
print("THIS PROGRAM IS WRITEN BY VAANI, ERP:- 162")
THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
