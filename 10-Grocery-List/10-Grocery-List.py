#-----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     To add items to a pre-made grocery list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
 Grocery_List = []
 print("Welcome to the SuperMarket Mania!")
 print("Your grocery list is empty.")

 while True:
     Add_Item = input("Would you like to add an item to your grocery list? (yes/no): ")

     if Add_Item.strip().lower() == "yes":
         Add_Item = input("Enter the item you would like to add: ")
         Grocery_List.append(Add_Item)
         print(f"The item '{Add_Item}' has been added to your grocery list.")
     elif Add_Item.strip().lower() == "no":
         # Asking if the user wants to view the list
         Affirm = input("Would you like to view your grocery list? (yes/no): ")
         if Affirm.strip().lower() == "yes":
             if len(Grocery_List) == 0:
                 print("Your grocery list is empty.")
             else:
                 print("Your grocery list contains:")
                 print(Grocery_List)
         break  # Exit the loop after the user is done
     else:
         print("Invalid input. Please answer with 'yes' or 'no'.")