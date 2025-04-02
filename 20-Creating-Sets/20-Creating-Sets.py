# Print a message to indicate the start of the program
print("Create a set")
print("Please enter the elements of the set")

# Collect user input for six elements
x = input("Enter the first element of the set: ")  # Get first element
y = input("Enter the second element of the set: ")  # Get second element
z = input("Enter the third element of the set: ")  # Get third element
a = input("Enter the fourth element of the set: ")  # Get fourth element
b = input("Enter the fifth element of the set: ")  # Get fifth element
c = input("Enter the sixth element of the set: ")  # Get sixth element

# Create a set with the input values (duplicates, if any, will be removed)
fruit_basket = {x, y, z, a, b, c}

# Print the elements of the set
print("The elements of the set are:", fruit_basket)
