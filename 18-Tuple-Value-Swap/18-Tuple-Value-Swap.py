#-----------------------------------------------------------------------------
# Name:       Value swap
# Purpose:     To witch around values of a tuple
#
# Author:      Aarvish Gupta
# Created:     26-Mar-2025
# Updated:     27-Mar-2025
#-----------------------------------------------------------------------------
# Ask the user to input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Store them in a tuple
values = (num1, num2)

# Swap values using tuple unpacking
num1, num2 = num2, num1

# Print the swapped values
print(f"Swapped values: ({num1}, {num2})"