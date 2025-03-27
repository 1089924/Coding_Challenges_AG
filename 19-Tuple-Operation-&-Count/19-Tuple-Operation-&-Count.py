#-----------------------------------------------------------------------------
# Name:        Tuples operation
# Purpose:     Count the number of a certain values in a tuple
#
# Author:      Aarvish Gupta
# Created:     26-Mar-2025
# Updated:     27-Mar-2025
#-----------------------------------------------------------------------------
# Step 1: Create a tuple with repeated values
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Step 2: Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ").strip().lower()

# Step 3: Count occurrences and display the result
count = fruits.count(fruit_name)

print(f"'{fruit_name}' appears {count} times in the tuple.")
