    BEGIN
    Initialize grocery_list with ['apples', 'bananas', 'carrots', 'milk', 'bread']
    Print grocery_list
    
    Prompt user: "Which item would you like to edit?"
    Read input into Edit
    
    Prompt user: "Enter a new item to add to the list:"
    Read input into edit
    
    Replace the item in grocery_list at index of Edit with edit
    Print confirmation message: "The edit from Edit to edit was successful!"
    
    Prompt user: "Would you like to view the updated list?"
    Read input into Affirmation
    
    IF Affirmation is "yes" THEN
        Print grocery_list
    ELSE
        Print "Thank you for using our service."
    ENDIF
    END
