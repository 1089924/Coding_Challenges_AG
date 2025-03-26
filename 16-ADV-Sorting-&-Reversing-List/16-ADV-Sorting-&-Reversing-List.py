#-----------------------------------------------------------------------------
# Name:        Reversing the items of a list
# Purpose:     To reverse the items in a said list
#
# Author:      A.Gupta
# Created:     19-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------

# Initialize a list of fruits
Fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Pineapple', 'Peach']

# Sort the list in alphabetical order
Fruits_alphabetical = sorted(Fruits)
# Sort the list in reverse alphabetical order
Fruits_reverse = sorted(Fruits, reverse=True)

# Print the sorted lists
print(Fruits_alphabetical)
print(Fruits_reverse)