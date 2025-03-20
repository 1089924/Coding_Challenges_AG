
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors)

num1=int(input("Enter the number of the element before the element you want to extract:"))
num2=int(input("Enter the number of the second element that you want to extract:"))

sliced_colours = (colors[num1:num2])

print (colors[num1:num2])

length_of_colors = len(colors)
print("The length of the initial list is ",length_of_colors)