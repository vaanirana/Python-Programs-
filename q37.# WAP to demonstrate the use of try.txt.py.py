# WAP to demonstrate the use of try, except & else

try:
   number = int(input("Enter an integer number: "))

   result = number / 10 

except ZeroDivisionError:

    print("Error: Cannot divide by zero")

except ValueError:

    print ("Error: Enter a valid number")

else:

   print (f" & {number }/10: {int (result)}")

print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:- 162")THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
