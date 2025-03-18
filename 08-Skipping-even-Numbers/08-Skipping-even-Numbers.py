# Loop through numbers from 1 to 10
for num in range(1, 11):
    # Check if the number is even
    if num % 2 == 0:
        continue  # Skip the current iteration if the number is even
    print(num)  # Print the number if it is odd
