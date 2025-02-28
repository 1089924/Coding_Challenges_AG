#Print a user-friendly entry message
print("Welcome to the Temperature Advice App")
#Ask for the users input which is stored in the Temperature variable, using the float data type for whole-decimal values
Temperature = float(input("What is the current temperature? "))
# Conditionals
#If statement for Temperature that is less then 10 and more than 25
if Temperature < 25 and Temperature > 10:
    print("It's a nice day. Wear short-sleeves!.")
#If statement for Temperature that is less then 10
elif Temperature < 10:
    print("It's cold outside.Wear a jacket!.")
#If statement for Temperature that is more than 25
elif Temperature > 25:
    print("It's hot outside. Stay cool!.")
    #Print a user-friendly exit message
print("Have a nice day!")
