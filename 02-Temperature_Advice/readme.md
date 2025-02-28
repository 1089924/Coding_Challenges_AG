Welcome the user to the application 

    print("Welcome to the Temperature Advice App")

Take the users input as a "Float" in case Temperature is a decimal value

    Temperature = float(input("What is the current temperature? "))

Conditionals:

Condition of message is the temperature is between the two extreme values of 25 and 10

    if Temperature < 25 and Temperature > 10:

    print("It's a nice day. Wear short-sleeves!.")


Condition of message is the temperature is less than 10

    elif Temperature < 10:

    print("It's cold outside.Wear a jacket!.")

Condition of message is the temperature is more than 25


    elif Temperature > 25:

    print("It's hot outside. Stay cool!.")

Print a user-friendly ending message

    print("Have a nice day!")