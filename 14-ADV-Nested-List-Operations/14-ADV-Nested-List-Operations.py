
# Initial list of students
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]

# Function to display the current students' data
def display_students():
    print("\nCurrent students list:")
    for student in students:
        print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

# Function to update Bob's data
def update_student_data():
    print("\nLet's update Bob's data!")
    new_age = int(input("Enter Bob's new age: "))
    new_major = input("Enter Bob's new major: ")

    # Finding Bob in the list and updating his age and major
    for student in students:
        if student[0] == 'Bob':
            student[1] = new_age
            student[2] = new_major
            print("\nBob's data has been updated.")
            break

# Function to find and print the student studying 'Biology'
def print_biology_student():
    for student in students:
        if student[2] == 'Biology':
            print(f"\nThe student studying Biology is: {student[0]}")
            break

# Main program
def main():
    display_students()

    update_student_data()  # Allow the user to update Bob's data

    print("\nUpdated list of students:")
    display_students()  # Print the updated student list

    print_biology_student()  # Print the name of the student studying Biology

# Run the program
if __name__ == "__main__":
    main()
