#-----------------------------------------------------------------------------
# Name:        Guessing the number game
# Purpose:     Random number guessing game
#
# Author:      Aarvish Gupta
# Created:     16-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

# Start the guessing game
while True:
    # Ask the user to guess the number
    user_guess = int(input("Guess the number: "))

    # Check if the guess is correct
    if user_guess == number_to_guess:
        print("Correct! 🎉")
        break  # Exit the loop if the guess is correct
    else:
        print("Wrong, try again!")
