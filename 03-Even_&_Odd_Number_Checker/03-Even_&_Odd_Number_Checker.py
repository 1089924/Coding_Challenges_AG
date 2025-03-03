#-----------------------------------------------------------------------------
# Name:        Even-Odd number checker
# Purpose:     To classify numbers between odd and even
#
# Author:      Aarvish Gupta
# Created:     24-Feb-2025
# Updated:     03-Mar-025
#-----------------------------------------------------------------------------

#Print a user-friendly entry message
print("Hey,Welcome to Even & Odd Number Checker")
#Take the users input in the integer data type
number = int(input("Enter a number: "))
#Using conditionals to check if the remainder of the division of our variable with two is zero
if number % 2 == 0:
    print("The number is Even")
# if the remainder is not Zero the nuber is odd
else:
    print("The number is Odd")
#Print a user-friendly exit message
print("Thank you for using our application")
