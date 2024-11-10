Ques-33 write a python code to print all the Armstrong number in a given range also calculate and display the total count

def is_armstrong_number(number):
    #Convert the number to a string to easily iterate through digits
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number
number = int(input("Enter a number:"))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:- 162")
