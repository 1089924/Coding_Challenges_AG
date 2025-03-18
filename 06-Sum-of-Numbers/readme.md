Ask the user a number input whiich is stored in the variable "n" and is the integer data type

    n = int(input("Enter a number: "))

Store the sum in the variable "total_sum" and initialize the loop to zero 

    total_sum = 0  # Initialize the sum

 Declare the range of the input integers stored in the variable "n"

    for i in range(1, n + 1):

Declare the loop "+=i" which loops the system till our input number and sums all of them up

        total_sum += i

Finally, print out the total sum of the number range 

    print(f"Sum = {total_sum}")
