#trignomatery operations in python
import math
x = float(input("enter a vlaue for x : < 1 check trignometry functions in python :"))
y = float(input("enter a vlaue for y : <= 1 check trignometry functions in python :"))
z = float(input("enter a vlaue for z : <=>1 check trignometry functions in python :"))
if x < 1 and y <= 1:
# if x < 1 or y <= 1:
    print("arc sin/cos/tan == > inverse of sin cos tan")
    print("acos(",x,") :",math.acos(x)) #if x>1 ==> math domain error
    print("asin(",y,") :",math.asin(y)) #if y>1 ==> math domain error
    print("atan(",z,") :",math.atan(z)) 
    print("tan2=tan(x/y) -> atan2(",x,",",y,")",math.atan2(x,y))
    print("cos(",y,") : ",  math.cos(y))
    print ("x*x + y*y (Euclidean form) -->hypot(",x,",",y,") : ",  math.hypot(x, y)) 
    print("sin(",x,") : ",math.sin(x))
    print("tan(",z,") : ",math.tan(z))
    print("radian -> degrees..degree(3) : ",  math.degrees(3))
    print("degree to radians >> radians(0.5) : ",  math.radians(0.5))
else:
    print("invalid input value must be x < 1 & y <=1 ")
