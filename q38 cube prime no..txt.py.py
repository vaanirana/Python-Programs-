#write a python code to print sum of cube of t prime numbers in a given range
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_cubes_of_primes(start, end):
    """Calculate the sum of cubes of all prime numbers in the given range."""
    total_sum = 0
    for number in range(start, end + 1):
        if is_prime(number):
            total_sum += number ** 3
    return total_sum

# Example usage
start_range =1
end_range = 5
result = sum_of_cubes_of_primes(start_range, end_range)
print(f"The sum of the cubes of all prime numbers between {start_range} and {end_range} is: {result}")
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:- 162")
