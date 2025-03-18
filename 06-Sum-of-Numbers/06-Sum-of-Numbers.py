def calculate_sum():
    # Ask the user for a number
    n = int(input("Enter a number: "))
    total_sum = 0  # Initialize the sum

    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        total_sum += i  # Add each number to the running total

    # Print the result
    print(f"Sum = {total_sum}")


calculate_sum()