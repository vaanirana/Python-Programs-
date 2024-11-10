def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def calculate_discount_and_final_bill(bill_amount):
    bill_amount_int = int(bill_amount)  # Convert to integer to avoid decimal point issues
    if bill_amount_int <= 10000:
        discount_percentage = sum_of_digits(bill_amount_int) / 2
    else:
        discount_percentage = sum_of_digits(bill_amount_int)

    discount_amount = (discount_percentage / 100) * bill_amount
    final_bill = bill_amount - discount_amount

    return discount_percentage, final_bill


# Example usage
bill_amount = float(input("Enter the bill amount: "))
discount_percentage, final_bill = calculate_discount_and_final_bill(bill_amount)

print(f"Discount Percentage: {discount_percentage}%")
print(f"Final Bill Amount: ₹{final_bill:.2f}")
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:- 162")
