# PROGRAM TO DEMONSTRATE NESTED ELSE-IF
myAge = input("Enter age: ")
myAge = int(myAge)

if myAge >= 18:
    myComment = "you can vote."
else:
    if myAge >= 10:
        myComment = "You are in middle school."
    else:
        if myAge >= 6:
            myComment = "You are in primary school."
        else:
            myComment = "You are too small to learn python:"
print("At age: " + str(myAge) + "->" + myComment)
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162")






THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162
