BEGIN  
    PRINT "Enter first number: "  
    READ num1  
    PRINT "Enter second number: "  
    READ num2  

    // Store values in a tuple  
    values ← (num1, num2)  

    // Swap values using tuple unpacking  
    num1, num2 ← num2, num1  

    // Print swapped values  
    PRINT "Swapped values: (", num1, ",", num2, ")"  
END  
