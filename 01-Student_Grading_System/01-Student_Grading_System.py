#Ask the user for their score.
print("Hey, Please input your grade for this terms ICS3U Program")
# The score is an integer input field.
myGrade = int(input("Score: "))
#using conditionals to obtain the desired output.
if myGrade >= 90:
    print("Grade: A")
elif myGrade >= 70 <= 79 :
     print("Grade: C")
elif myGrade >= 60 <= 69 :
     print("Grade: D")
else :
    print("Grade: F")
# User-friendly thank you message.
print("Thank you for sharing your grade")

