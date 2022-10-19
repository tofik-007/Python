a =15
b = 25
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print("==")
if ( a == b ):
 print (a," is equal to ",b)
else:
 print (a,"is not equal to ",b)

print("!=")
if ( a != b ):                          #<> is not supported in python 3.
    print (a,"is not equal to ",b)
else:
    print (a," is equal to ",b)

print("<")
if ( a < b ):
 print (a," is less than ",b) 
else:
 print (a,"is not less than ",b)

print(">")
if ( a > b ):
 print (a,"is greater than ",b)
else:
 print (a," is not greater than ",b)

print("<=")
if ( a <= b ):
 print (a,"is either less than or equal to",b)
else:
 print (a,"is neither less than nor equal to",b)

print(">=")
if ( b >= a ):
 print (a,"is either greater thanor equal to ",b)
else:
 print (a,"is neither greater thannor equal to ",b)