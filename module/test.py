from cmath import e, pi
from re import X
import mymodule
mymodule.greeting("Jonathan")

a = mymodule.person["age"]
print("age is : ",a)

b = mymodule.person["country"]
print("Country is : ",b)

c = mymodule.person["name"]
print("name is : ",c)


import cmath
from cmath import e
print("value of e is",e)
print("value of pie is",cmath.pi)
content = dir(cmath)
print (content)