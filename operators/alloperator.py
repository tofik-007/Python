'''the extra use of if elif else statement makes the all operators combine in the 1 program '''
print("1-arithematic operator")
print("2-Comparison (Relational) Operators")
print("3-Assignment Operators")
print("4-Logical Operators")
print("5-Bitwise Operators")
print("6-Membership Operators")
print("7-identity Operators")
print("8-Operators presedence")
Oprtor = int(input("enter a number from above options: ")) # i didn't specify type of input at the start.
if Oprtor == 1:
    print("this is showing arithematic operators: ")
    a = int(input("enter a number:"))
    b = int(input("enter a number : "))
    print("the addition is :",a+b)
    print("the subtraction is :",a-b)
    print("the multipication is :",a*b)
    print("the division is :",a/b)
    print("the modulo is :",a%b) #remainder
    print("the floor is :",a//b) #floor division contains whole number without point
    print("the exponent is :",a**b)
elif Oprtor == 2:
    print("this is showing comparison operators : ")
    a =15
    b = 25
    print(a==b)
    print(a!=b)
    print(a>b)
    print(a<b)
    print(a<=b)
    print(a>=b)
    a = int(input("enter a number to the assign a "))
    b = int(input("enter a number to the assign b "))
    c = int(input("enter a number to the assign c "))

    if ( a == b ):
        print ("1 a is equal to b")
    else:
        print ("1 a is not equal to b")

    if ( a != b ):
        print ("2 a is not equal to b")
    else:
        print ("2 a is equal to b")

    '''if ( a != b ):
    print ("3 a is not equal to b")
    else:
    print ("3 a is equal to b")'''

    if ( a < b ):
        print ("4 a is less than b") 
    else:
        print ("4 a is not less than b")

    if ( a > b ):
        print ("5 a is greater than b")
    else:
        print ("5 a is not greater than b")
    a = 5
    b = 20
    if ( a <= b ):
        print ("6 a is either less than or equal tob")
    else:
        print ("6 a is neither less than nor equal tob")

    if ( b >= a ):
        print ("7 b is either greater thanor equal to b")
    else:
        print ("7 b is neither greater thannor equal to b")
elif Oprtor == 3:
    print("this is showing Assignment Operators")
    a = 5
    b = 15
    c = a + b
    c += 5
    c -= 5
    c *= 5
    c /= 5
    print(c)
    print('hi') if a < b else print('hi')
    print('a & b are equal') if a == b else print('a & b are not equal')
elif Oprtor == 4:
    print("this is showing logical operator : ")
    a = 10
    b = 20
    c = 25
    if a == b & b < c:
        print("boat")
    else:
        print("1 condition is wrong")

    if a == b | b > c:
        print("boat")
    else:
        print("1 condition is right atleast")

    print(type(a & b))
    print(a & b)
elif Oprtor == 5:
    print("this is showing Bitwise Operators")
    a = 5 
    b = 10
    if a < b and a > b: #&
        print("either 1 condition is true ")
    else:
        print("or needed ")
    x = 101
    y = 201
    if a < b or a > b: #  |
        print("either 1 condition is true ")
    else:
        print("or needed ")
    a = 10
    b = 20
    if a < b | a > b: #|
        print("1 condition should be right")
    else:
        print("none")
    print(a ^ b) 
    print(~a ) 
    c = a << 2
    print(c) 
elif Oprtor == 6:
    print("this is showing the Membership Operators")
    print("given list is ")
    print([1, 2, 3, 4, 5, 6, 7, 8, 9])
    num1 = int(input("enter a number to find it in above list : "))
    num2 = int(input("enter a number to not find it in above list : "))
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if num1 in s:
        print(num1," is in the list")
    else:
        print(num1," is  not in list")
    if num2 in s:
        print(num2," is in the list")
    else:
        print(num2," is  not in the list")
    s1 = [14, 22, 73, 46, 25, 69, 72, 80, 89]
    print(s1)
    num3 = int(input("enter a nbumber to check availablity in the list: "))
    if num3 in s1:
        print(num3, "is in list list")
    else:
        print(num3,"is not in list")
    num4=int(input("enter a nbumber to check availablity in the list: "))
    if num4 not in s1:
        print("not present")
    else:
        print("present")
elif Oprtor == 7:
    print("this  is showing the identity operators : ")
    a = int(input("enter a number 4 a :"))
    b = int(input("enter a number 4 b :"))
    if (a is b):
        print("a & b has same identity")
    else:
        print("a & b is not same")

    x = int(input("enter a number 4 x :"))
    y = int(input("enter a number 4 y :"))
    if (a is not b):
        print("a & b doesn't have same identity ")
    else:
        print("a & b have same identity")
elif Oprtor == 8:
    print("this is showing the operator presedence : ")
    print("enter 4 numbers to perform the operations ")
    a = int(input("enter a number a:"))
    b = int(input("enter a number b:"))
    c = int(input("enter a number c:"))
    d = int(input("enter a number d:"))

    x = (a + b) * c / d       
    print ("Value of (a + b) * c / d is ",  x)

    y = ((a + b) * c) / d     
    print ("Value of ((a + b) * c) / d is ",  y)

    z = (a + b) * (c / d);    
    print ("Value of (a + b) * (c / d) is ",  z)

    t = a + (b * c) / d;      
    print ("Value of a + (b * c) / d is ", t) 
print("end of  operators")