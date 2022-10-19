#math function in python
import math
from cmath import exp, sqrt
from math import ceil
x = float(input("enter a number to check all the math function in python :->"))
print("entered number is ",x)
print("absolute value of abs(x)", x , "is",abs(x)) #----absolute value
print("ceil(x)gives nearest int >x : -->",ceil(x)) #---> 
# cmp() does not work in python 3. 
print("exponents of ",x ,"is" ,exp(x))  #exponent 
#floor: The floor of x: the smallest nearest integer <x
print ("math.floor(x)gives nearest int <x : --> ",x ,"is", math.floor(x)) #--> 100
#log
print("log of ",x,"is ",math.log(x))
print("log10 of ",x,"is ",math.log10(x))
y = float(input("enter a float number to check modf's use :->"))
print ("split both numbers before & after of",y,"is",math.modf(y))
#pow --> power
print ("pow(x)",x," with power of 5 is :->", math.pow(x,5))
print("round --> after the (a.b) how many numbers should be print is determine by it.")
a = float(input("enter a float for a in round function :->"))
b = int(input("enter an int for b in round function :->"))
print("round(",a,",",b,") :", round(a, b))
#sqrt --> square root
print("square root of ", x ,sqrt(x))