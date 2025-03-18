#-----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:     To provide the Grade on the basis of the numerical marks
#
# Author:      Aarvish Gupta
# Created:     16-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------

# Loop through numbers from 1 to 10
for num in range(1, 11):
    # Check if the number is even
    if num % 2 == 0:
        continue  # Skip the current iteration if the number is even
    print(num)  # Print the number if it is odd
