#-----------------------------------------------------------------------------
# Name:        Voting Eligibility Checker
# Purpose:     To check if you are og elligible age to vote
#
# Author:      Aarvish Gupta
# Created:     24-Feb-2025
# Updated:     03-Mar-025
#-----------------------------------------------------------------------------

#Output a user-friendly entry message
print("Welcome to the Voting Eligibility Checker App!")
# Store the input in the uAge variable as an integer data type
uAge = int(input("What year are you born? "))
# conditionals if the Age is higher than 18 you are eligible to vote
if uAge >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are too young to vote.")
# Print a user-friendly exit message
print("Thank you for using our application.")