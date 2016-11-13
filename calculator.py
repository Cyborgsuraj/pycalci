# Addition Function


def addition():
    add1 = float(input("enter the 1st number\t"))
    add2 = float(input("enter the 2nd number\t"))
    add = add1 + add2
    print "the addition answer is", add


# Subtraction Function

def subtraction():
    sub1 = float(input("enter the 1st number\t"))
    sub2 = float(input("enter the 2nd number\t"))
    sub = sub1 - sub2
    print "the subtraction answer is", sub


# Multiplication Function

def multiplication():
    multi1 = float(input("enter the 1st number\t"))
    multi2 = float(input("enter the 2nd number\t"))
    multi = multi1 * multi2
    print "the multiplication answer is", multi


# Division Function

def division():
    div1 = float(input("enter the dividend\t"))
    div2 = float(input("enter the divisor\t"))
    if div2 == 0:
        print"Division is not possible by zero\n"
        print"please change the divisor"
        exit(0)
    else:
        div = div1 / div2
        print"the division answer is", div


# Main Function

print"Simple Calculator\n\n"
print"Enter Your Option\n"
print"1)Addition 2)Subtraction 3)Multiplication 4)Division\t"
option = int(input())
if option == 1:
    print"Addition is selected\n"
    addition()
elif option == 2:
    print"Subtraction is selected\n"
    subtraction()
elif option == 3:
    print"Multiplication is selected\n"
    multiplication()
elif option == 4:
    print"Division is selected\n"
    division()
else:
    print"Please Select From The Option and Try Again\n"
    exit(0)

# End of program

print "\nPlease Support The Developers\n"
print "\nUse OpenSource Software\n"
print "\nThank you For using the Calculator\n"
