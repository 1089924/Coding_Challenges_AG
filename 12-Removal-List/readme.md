    BEGIN
        Initialize todo_list with ['write email', 'finish homework', 'call mom', 'clean room']
        Print todo_list
        
    Prompt user: "Enter the item to remove from the list:"
    Read input into item_to_remove
    
    IF item_to_remove is in todo_list THEN
        Remove item_to_remove from todo_list
        Print updated todo_list
    ELSE
        Print "'{item_to_remove}' is not in the list."
    ENDIF
    
    Prompt user: "Would you like to remove more items? (yes/no):"
    Read input into inp
    
    IF inp is "yes" THEN
        Prompt user: "Enter another item to remove from the list:"
        Read input into item_to_remove
        
        IF item_to_remove is in todo_list THEN
            Remove item_to_remove from todo_list
            Print updated todo_list
        ELSE
            Print "'{item_to_remove}' is not in the list."
        ENDIF
    ELSE
        Print "Thank you for using our service."
    ENDIF
    END

