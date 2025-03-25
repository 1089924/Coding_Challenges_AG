BEGIN
    Initialize students list with [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]
    
    FUNCTION display_students():
        PRINT "Current students list:"
        FOR each student in students:
            PRINT "Name: student[0], Age: student[1], Major: student[2]"
    
    FUNCTION update_student_data():
        PRINT "Let's update Bob's data!"
        PROMPT "Enter Bob's new age:"
        READ input into new_age
        PROMPT "Enter Bob's new major:"
        READ input into new_major
        
        FOR each student in students:
            IF student[0] == 'Bob' THEN
                UPDATE student[1] with new_age
                UPDATE student[2] with new_major
                PRINT "Bob's data has been updated."
                BREAK
            ENDIF
        ENDFOR
    
    FUNCTION print_biology_student():
        FOR each student in students:
            IF student[2] == 'Biology' THEN
                PRINT "The student studying Biology is: student[0]"
                BREAK
            ENDIF
        ENDFOR
    
    FUNCTION main():
        CALL display_students()
        CALL update_student_data()
        PRINT "Updated list of students:"
        CALL display_students()
        CALL print_biology_student()
    
    CALL main()
END
