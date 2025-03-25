#-----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     To add items to a pre-made grocery list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
# Initialize an empty grocery list
Grocery_List = []

# Welcome message
print("Welcome to the SuperMarket Mania!")
print("Your grocery list is empty.")

# Infinite loop to keep asking the user for input
while True:
    # Ask the user if they want to add an item
    Add_Item = input("Would you like to add an item to your grocery list? (yes/no): ")

    # Check if the user wants to add an item
    if Add_Item.strip().lower() == "yes":
        Add_Item = input("Enter the item you would like to add: ")  # Get the item name
        Grocery_List.append(Add_Item)  # Add item to the list
        print(f"The item '{Add_Item}' has been added to your grocery list.")

    # Check if the user does not want to add an item
    elif Add_Item.strip().lower() == "no":
        # Ask if the user wants to view the list before exiting
        Affirm = input("Would you like to view your grocery list? (yes/no): ")

        if Affirm.strip().lower() == "yes":
            # Check if the list is empty
            if len(Grocery_List) == 0:
                print("Your grocery list is empty.")
            else:
                print("Your grocery list contains:")
                print(Grocery_List)  # Display the list

        break  # Exit the loop after the user is done

    # Handle invalid inputs
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
