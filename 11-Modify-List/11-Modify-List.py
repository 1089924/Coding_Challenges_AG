# -----------------------------------------------------------------------------
# Name:        List Modification
# Purpose:     To make changes into a preset list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
# -----------------------------------------------------------------------------

# Initialize a grocery list with some items
grocery_list = ['apples', 'bananas', 'carrots', 'milk', 'bread']

# Print the initial grocery list
print(grocery_list)

# Ask the user which item they would like to edit
Edit = input("Which item would you like to edit? ")

# Ask for the new item to replace the old one
edit = input("Enter a new item to add to the list: ")

# Find the index of the item to be edited and replace it with the new item
grocery_list[grocery_list.index(Edit)] = edit

# Confirm that the edit was successful
print("The edit from", Edit, "to", edit, "was successful!")

# Ask the user if they want to view the updated list
Affirmation = input("Would you like to view the updated list: ")
if Affirmation.strip().lower() == "yes":
    print(grocery_list)  # Print updated list
else:
    print("Thank you for using our service.")