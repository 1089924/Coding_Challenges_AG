BEGIN
    Initialize numbers list with [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Initialize numbers_even as an empty list
    Initialize numbers_squared as an empty list
    
    PRINT numbers
    
    FOR each number in numbers:
        IF number is even THEN
            REMOVE number from numbers list
            APPEND number to numbers_even list
        ENDIF
    ENDFOR
    
    PRINT numbers_even