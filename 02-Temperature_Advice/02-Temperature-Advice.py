#Print a user-friendly entry message
print("Welcome to the Temperature Advice App")
#Ask for the users input
Temperature = float(input("What is the current temperature? "))
# Conditionals to get the desired output
if Temperature < 25 and Temperature > 10:
    print("It's a nice day. Wear short-sleeves!.")
elif Temperature < 10:
    print("It's cold outside.Wear a jacket!.")
elif Temperature > 25:
    print("It's hot outside. Stay cool!.")
    #Print a user-friendly exit message
print("Have a nice day!")
