#-----------------------------------------------------------------------------
# Name:        List Filtering
# Purpose:     To manipulate the items of a list to obtain our required output
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------

# Initialize a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Initialize an empty list for even numbers
numbers_even = []
# Initialize an empty list for squared even numbers
numbers_squared = []

# Print the initial list of numbers
print(numbers)

# Iterate through the numbers list to find even numbers
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)  # Remove even numbers from the original list
        numbers_even.append(number)  # Add even numbers to the numbers_even list

# Print the list of even numbers
print(numbers_even)

# Iterate through the even numbers list and calculate their squares
for number in numbers_even:
    numbers_squared.append(number**2)

# Print the squared values of even numbers
print(numbers_squared)