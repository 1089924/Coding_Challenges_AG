#Ask the user for their score.
print("Hey, Please input your grade for this terms ICS3U Program")
# The score is an integer input field.
myGrade = int(input("Score: "))
#Conditionals
# If-Statement 1 to get Grade A
if myGrade >= 90:
   print("Grade: A")
# If-Statement 2 to get Grade B
elif myGrade >= 80 <= 89 :
    print("Grade: B")
# If-Statement 3 to get Grade C
elif myGrade >= 70 <= 79 :
    print("Grade: C")
# If-Statement 4 to get Grade D
elif myGrade >= 60 <= 69:
   print("Grade: D")
# If-Statement 4 to get Grade E
elif myGrade >= 50 <= 59:
   print("Grade: E")


#Ending else statement for Grade F
else :
   print("Grade: F")
# User-friendly thank you message.
print("Thank you for sharing your grade")
