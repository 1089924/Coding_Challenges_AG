#-----------------------------------------------------------------------------
# Name:       List Slicing
# Purpose:    To edit the list to obtain the required values from the main list
#
# Author:      Aarvish Gupta
# Created:     19-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------

# Initialize a list of colors
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Print the initial list of colors
print(colors)

# Ask the user for indices to extract a slice from the list
num1 = int(input("Enter the number of the element before the element you want to extract:"))
num2 = int(input("Enter the number of the second element that you want to extract:"))

# Extract the slice from the list
sliced_colours = colors[num1:num2]

# Print the extracted slice
print(colors[num1:num2])

# Calculate and print the length of the original list
length_of_colors = len(colors)
print("The length of the initial list is", length_of_colors)
