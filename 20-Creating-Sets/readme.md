BEGIN
    PRINT "Create a set"
    PRINT "Please enter the elements of the set"

    INPUT x  ← "Enter the first element of the set"
    INPUT y  ← "Enter the second element of the set"
    INPUT z  ← "Enter the third element of the set"
    INPUT a  ← "Enter the fourth element of the set"
    INPUT b  ← "Enter the fifth element of the set"
    INPUT c  ← "Enter the sixth element of the set"

    CREATE a set fruit_basket containing {x, y, z, a, b, c}

    PRINT "The elements of the set are:", fruit_basket
END
