# Exercise 2: Logical Operators

# Create a program that checks if a number is within the range of 10 to 20 (inclusive). 
# Print "In range" if it is, and "Out of range" if it isn't. 
# Remember to test your program using different numbers to ensure you get the correct output.

number = int(input("Enter a number: "))

if number >= 10 and number <= 20:
    print("In range")
else:
    print("Out of range")