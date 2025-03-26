#-----------------------------------------------------------------------------
# Name:        Removal of Lists
# Purpose:     To remove items from a list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------

# Initialize a to-do list with some tasks
todo_list = ['write email', 'finish homework', 'call mom', 'clean room']

# Print the initial to-do list
print(todo_list)

# Ask the user which item they want to remove
item_to_remove = input("Enter the item to remove from the list: ")

# Check if the item exists in the list and remove it if found
if item_to_remove in todo_list:
    todo_list.remove(item_to_remove)
    print(todo_list)  # Print the updated list
else:
    print(f"'{item_to_remove}' is not in the list.")

# Ask the user if they want to remove more items
inp = input("Would you like to remove more items? (yes/no): ").strip().lower()

if inp == 'yes':
    item_to_remove = input("Enter another item to remove from the list: ")

    if item_to_remove in todo_list:
        todo_list.remove(item_to_remove)
        print(todo_list)  # Print the updated list
    else:
        print(f"'{item_to_remove}' is not in the list.")
else:
    print("Thank you for using our service.")
