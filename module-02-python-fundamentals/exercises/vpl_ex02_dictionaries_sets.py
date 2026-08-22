# Exercise 2: Dictionaries and Sets

# Write a Python program that creates a dictionary to store information about a person (name, age, city). 
# Then create a set of hobbies for that person. Finally, print both the dictionary and the set.

# Note:

# If the person's name is "Alice", age is 30, and city is "New York"

# The output should be:

# Person Info: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Hobbies: {'reading', 'swimming'}

person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

hobbies = {"reading", "swimming"}

print("Person Info:", person_info)

print("Hobbies:", hobbies)