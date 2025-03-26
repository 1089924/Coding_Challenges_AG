# -----------------------------------------------------------------------------
# Name:        List Modification
# Purpose:     To allow a user to modify items in a preset grocery list.
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Name:        Modify List
# Purpose:     To make changes in a list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
# -----------------------------------------------------------------------------

# Initialize a grocery list with some default items
grocery_list = ['apples', 'bananas', 'carrots', 'milk', 'bread']

# Display the initial grocery list
print("Current Grocery List:", grocery_list)

# Prompt the user to enter the item they want to replace
Edit = input("Which item would you like to edit? ")

# Ask for the new item to replace the old one
edit = input("Enter a new item to add to the list: ")

# Check if the item exists in the list before attempting to modify it
if Edit in grocery_list:
    grocery_list[grocery_list.index(Edit)] = edit  # Replace the item
    print(f"The edit from '{Edit}' to '{edit}' was successful!")  # Confirm change
else:
    print(f"'{Edit}' not found in the list. No changes were made.")  # Handle invalid input

# Ask if the user wants to see the updated list
Affirmation = input("Would you like to view the updated list? (yes/no): ").strip().lower()

# Display the updated list if the user says "yes"
if Affirmation == "yes":
    print("Updated Grocery List:", grocery_list)
else:
    print("Thank you for using our service.")
