#Write Python Program to Count the Total Number of Vowels, Consonants and Blanks in a String
def main():
    # Get input from the user
    user_string = input("Enter a string: ")
    
    # Initialize counters for vowels, consonants, and blanks
    vowels = 0
    consonants = 0
    blanks = 0
    
    # Define a set of vowels for easier comparison
    vowel_set = "aeiouAEIOU"
    
    # Traverse each character in the user string
    for each_character in user_string:
        if each_character in vowel_set:
            vowels += 1
        elif each_character.isalpha():
            consonants += 1
        elif each_character == " ":
            blanks += 1
    
    # Print the results
    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")

# Ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:- 162")
THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
