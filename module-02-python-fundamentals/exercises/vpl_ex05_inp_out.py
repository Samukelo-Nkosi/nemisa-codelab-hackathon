# Exercise 5: Practising Input and Output Functions

# Write a Python program that does the following:
# Ask the user for their name and age.
# Calculates how many years until they turn 100 years old.
# Prints a message telling them how many years are left until they reach 100 years old.
# Ensure that you convert the age input from a string to an integer so that you can perform calculations. 
# Use comments to #explain each step of your program. Here is an example of what your output should look like:

# What is your name? Alice

# How old are you? 30

# Hello, Alice! You have 70 years until you turn 100.

name = input("What is your name? ")

age = int(input("How old are you? "))

years_left = 100 - age

print("Hello, " + name + "! You have", years_left, "years until you turn 100.")