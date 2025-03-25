BEGIN
    Initialize an empty list called Grocery_List
    Print "Welcome to the SuperMarket Mania!"
    Print "Your grocery list is empty."

    WHILE True DO
        Prompt user: "Would you like to add an item to your grocery list? (yes/no): "
        Read input into Add_Item

        IF Add_Item is "yes" THEN
            Prompt user: "Enter the item you would like to add: "
            Read input into Add_Item
            Append Add_Item to Grocery_List
            Print confirmation message
        ELSE IF Add_Item is "no" THEN
            Prompt user: "Would you like to view your grocery list? (yes/no): "
            Read input into Affirm

            IF Affirm is "yes" THEN
                IF Grocery_List is empty THEN
                    Print "Your grocery list is empty."
                ELSE
                    Print "Your grocery list contains:" 
                    Print Grocery_List
            ENDIF
            BREAK the loop
        ELSE
            Print "Invalid input. Please answer with 'yes' or 'no'."
        ENDIF
    ENDWHILE
END
