# pattern_drawing.py

# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after a row is printed
    row += 1
