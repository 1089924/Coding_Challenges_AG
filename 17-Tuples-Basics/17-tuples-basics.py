#-----------------------------------------------------------------------------
# Name:        Tuples
# Purpose:     Using tuples
#
# Author:      Aarvish Gupta
# Created:     26-Mar-2025
# Updated:     27-Mar-2025
#-----------------------------------------------------------------------------

# Display instructions to the user
print("Please provide the specific items for your list")
print("No changes can be made to the list once you have entered the values")

# Prompt the user for different types of inputs and store them in variables
print("Please enter an integer value:")
x_integr = int(input())  # Taking integer input

print("Please enter a float value:")
y_float = float(input())  # Taking float input

print("Please enter a string value:")
x_string = input()  # Taking string input

print("Please enter a Boolean value (True/False):")
y_bool = input()  # Taking boolean input as a string (Needs conversion if used logically)

print("Please enter a small list:")
x_list = input()  # Taking list input as a string (Not actually a list unless converted)

# Thank the user for their inputs
print("Thank you for your inputs")

# Create a tuple with all the collected values
Initial_tuple = (x_integr, y_float, x_string, y_bool, x_list)

# Ask the user if they want to view the tuple
print("Would you like to view your list?")
Affirmative = input()

# If the user says "Yes", display the tuple
if Affirmative == "Yes":
    print(Initial_tuple)
# Otherwise, print a thank-you message and exit
else:
    print("Thank you for using our application")
