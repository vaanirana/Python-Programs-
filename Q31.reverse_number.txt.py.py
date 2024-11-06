def reverse_number(n):
    # Handle negative numbers
    is_negative = n < 0
    n = abs(n)
    
    reversed_number = 0
    
    while n > 0:
        # Extract the last digit
        last_digit = n % 10
        # Append the last digit to the reversed_number
        reversed_number = reversed_number * 10 + last_digit
        # Remove the last digit from n
        n = n // 10
    
    # Restore the negative sign if necessary
    if is_negative:
        reversed_number = -reversed_number
    
    return reversed_number

# Example usage
number = 12345
print("Original number:", number)
print("Reversed number:", reverse_number(number))
THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
