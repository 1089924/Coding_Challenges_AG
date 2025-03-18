#-----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:     To provide the Grade on the basis of the numerical marks
#
# Author:      Aarvish Gupta
# Created:     16-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
# Countdown starting from 10
count = 10

while count > 0:
    print(count)
    user_input = input('Enter "stop" to cancel or press Enter to continue: ').strip()  # Get user input

    if user_input.lower() == "stop":
        print("Countdown stopped!")
        break  # Exit the loop if the user types "stop"

    count -= 1  # Decrease the countdown

# In case the countdown reaches 1 and no stop is given
if count == 0:
    print("Countdown finished!")

