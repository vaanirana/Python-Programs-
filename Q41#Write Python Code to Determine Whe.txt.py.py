#Write Python Code to Determine Whether the Given String Is a Palindrome or Not 
def main():
    # Get user input
    user_string = input("Enter string: ")
    
    # Check if the string is equal to its reverse
    if user_string == user_string[::-1]:
        print(f"User entered string is palindrome")
    else:
        print(f"User entered string is not a palindrome")

# Ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162")
