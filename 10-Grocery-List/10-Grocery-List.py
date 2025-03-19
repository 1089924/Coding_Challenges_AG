#-----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     To add items to a pre-made grocery list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------

Grocery_List = ['milk', 'eggs', 'bread', 'apples',]

Grocery = input("What do you want to buy today:")
Grocery_List.append(Grocery)

Grocery2 = input("What else do you want to buy today:")
Grocery_List.append(Grocery2)

print(Grocery_List)



