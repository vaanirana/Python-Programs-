q34. write a python code to print all the Armstrong number in a given range also calculate
display the total count
def is_armstrong_number(number):
    digits = str(number)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == number
def find_armstrong_in_range(start, end):
    armstrong_numbers = []
    for number in range(start, end + 1):
     if is_armstrong_number(number):
            armstrong_numbers.append(number)
    return armstrong_numbers
start_range = int(input("Enter the start of the range:"))
end_range = int(input("Enter the end of the range:"))
armstrong_numbers = find_armstrong_in_range(start_range, end_range)
print("Armstrong numbers in the range:", armstrong_numbers)
print("Total count of Armstrong numbers:", len(armstrong_numbers))
print("THIS PROGRAM IS WRITTEN BY VAANI,  ERP:-164")THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
