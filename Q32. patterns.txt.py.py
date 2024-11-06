1.# number of rows
rows = 5
# loop through the rows
for i in range(1, rows + 1):
    # print '*' i times
    print('*' * i)

2. # number of rows
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
     print(j, end='')
    print()

3.# number of rows
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
     print(i, end='')
    print()

4.# number of rows
rows = 5
# loop through the rows
for i in range(rows, 0,  -1):
    # print '*' i times
    print('*' * i)

5. # Number of rows in the pattern
rows = 5

# Outer loop will handle the number of rows
for i in range(rows):
    
    # Inner loop will handle the numbers in each row
    for j in range(rows, i, -1):
        print(j, end="")
    
    # Moving to the next line after each row
    print()


6. # number of rows
rows = 5
for i in range (rows, 0, -1):
    print(str(i) * i)

7. # number of rows
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)

8.# number of rows
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

9.# number of rows
rows = 5
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

10. # number of rows
rows = 5

# upper part of diamond
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

    # lower part of diamond
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
