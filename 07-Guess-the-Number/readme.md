
Import random for the generation of random numbers required for the loops. 

    import random

Input the range of the random number field into a variable for easy access; the data type is "int" as we are dealing with integers.

    number_to_guess = random.randint(1, 10)

Begin the "while" loop which is a constant condition on the data that is being inputted

    while True:
  
Store the users input in a variable using the "int" data type as we are dealing with numbers 
 
    user_guess = int(input("Guess the number: "))

Use a conditional to check if the number guessed is the same as the random number selected

    if user_guess == number_to_guess:
        print("Correct! 🎉")
If the guess is correct, The "break" command stops the loop and the data put in after the break is not put through the looping process
            
    break  
Finally, if the "if" condition is not followed; print an output message so that the whole looping process starts again.
    else:
        print("Wrong, try again!")

