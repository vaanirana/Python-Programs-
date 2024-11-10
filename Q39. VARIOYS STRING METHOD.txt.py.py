#Write a python program to demonstrate various string methods 

text = " Hello, World! "

# Changing case
lowercase_text = text.lower()  # " hello, world! "
uppercase_text = text.upper()  # " HELLO, WORLD! "
title_text = text.title()       # " Hello, World! "

# Trimming whitespace
stripped_text = text.strip()    # "Hello, World!"
words = stripped_text.split(",") # ['Hello', ' World!']
joined_text = "-".join(words)    # "Hello- World!"

# Replacing and finding
replaced_text = stripped_text.replace("World", "Python")  # "Hello, Python!"
index = stripped_text.find("World")                        # 7
count = stripped_text.count("o")                          # 2

# Output results
print(lowercase_text)
print(uppercase_text)
print(title_text)
print(stripped_text)
print(words)
print(joined_text)
print(replaced_text)
print(index)
print(count)
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162")
