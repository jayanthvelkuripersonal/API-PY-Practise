#Function is to find if the number of postive, negative or Zero#
#Funcation to check if it is square or not
def check_number(value):
    print("Please enter value to check ")
    #value=input()
    if value >= 0:
        print("Positive")
    else:
        print("negative")
def check_shape(side1, side2, side3, side4):
    print("Enter four sides")
    if side1 ==  side3 and side2 == side4:
        print("This is a square")
    elif side1 != side3 and side2 != side4:
        print("This is Not a square")
check_number()

