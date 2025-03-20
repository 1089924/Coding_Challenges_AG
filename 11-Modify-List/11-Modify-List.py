# -----------------------------------------------------------------------------
# Name:        List Modification
# Purpose:     To make changes into a preset list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
# -----------------------------------------------------------------------------

grocery_list = ['apples', 'bananas', 'carrots', 'milk', 'bread']

print(grocery_list)

Edit = input("Which item would you like to edit? ")

edit = input("Enter a new item to add to the list: ")

grocery_list[grocery_list.index(Edit)] = edit

print("The edit from", Edit, "to", edit, "was successful!")

Affirmation = input("Would you like to view the updated list: ")
if Affirmation.strip().lower() == "yes":
    print(grocery_list)
else:
    print("Thank you for using our service.")


