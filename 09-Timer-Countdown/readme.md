  
Start By initializing and declaring the "count" variable to 10; the total number of iterations are ten 

    count = 10

Begin the while loop declaring that it is greater than zero to initialise it 

    while count > 0:
output the count value 

    print(count)

 take the users input for the countdown, if they want to continue with it or stop it; the input is stored in a variable.

    user_input = input('Enter "stop" to cancel or press Enter to continue: ').strip()

Check if the users input is "stop", use the break command to end the looping process and output a message to show the user that the process has ended

    user_input.lower() == "stop":
        print("Countdown stopped!")
        break

Declare the count value to negative and equal to one to decrease the countdown by  value of one 

    count -= 1

Check if the count has reached zero, then output an exit message showing that the countdown has ended

    if count == 0:
    print("Countdown finished!")
