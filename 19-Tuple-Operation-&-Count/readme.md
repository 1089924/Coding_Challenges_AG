BEGIN  
    // Step 1: Create a tuple with repeated values  
    DEFINE fruits AS ("apple", "banana", "apple", "cherry", "banana", "apple")  
    
    // Step 2: Ask the user to enter a fruit name  
    PRINT "Enter a fruit name: "  
    INPUT fruit_name  
    
    // Step 3: Count occurrences of the fruit in the tuple  
    SET count TO fruits.count(fruit_name)  
    
    // Step 4: Display the result  
    PRINT "'" + fruit_name + "' appears " + count + " times in the tuple."  
END  
