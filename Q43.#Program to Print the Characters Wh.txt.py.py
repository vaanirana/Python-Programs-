#Program to Print the Characters Which Are Common in Two Strings
def common_characters(string_1, string_2):
    # Loop through each character in the first string
    for letter in string_1:
        # Check if the character is in the second string
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")

def main():
    # Call the function with two strings
    common_characters('rose', 'goose')

# Ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
print("THIS PROGRAM IS WRITTEN BY KAUSHAL, ERP:- 154")THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
