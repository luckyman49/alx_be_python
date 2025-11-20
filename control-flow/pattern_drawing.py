# pattern_drawing.py
# Objective: Draw a square pattern of asterisks using nested loops

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")  # print asterisk without newline
    print()  # move to next line after each row
    row += 1
