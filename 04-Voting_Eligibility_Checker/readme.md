Print a user-friendly entry message

    print("Welcome to the Voting Eligibility Checker App!")

Store the users input in a variable and put it in the integer field

    uAge = int(input("What year are you born? "))

Using conditionals to get the desired output: if you are greater an 18 you are eligible to vote   

    if uAge >= 18:
    print("You are eligible to vote!")
    else:
    print("Sorry, you are too young to vote.")

Print a user-friendly exit message 
    
    print("Thank you for using our application.") 