#Conditionals
var1 = 10
var2 = 20
if var1 < var2:
    print("var2 is greater than var1")

var3=int(input("Enter a number: "))

if var3 < var2:
    print("var3 is less than var2")

var4, var5 = 1, 2
#Conditional operations are and or and not
if var4==1 and var5==2:
    print("Both conditions are true")
    
if var4==1 or var5==2:
    print("At least one condition is true")
    
#else, elif and if statements

if var3 < var2:
    print("var3 is less than var2")
elif var3 == var2:
    print("var3 is equal to var2")
else:
    print("var3 is greater than var2")
    