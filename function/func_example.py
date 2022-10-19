#different function examples
def my_function(fname):
    """function to add name before last name :-> (programmer)"""
    print( fname + "programmer")
print(my_function.__doc__)
fname = input("enter first name : ")
my_function(fname)

def add(num1, num2):
	"""function to get sum of two numbers"""
	num3 = num1 + num2
	return num3
print(add.__doc__)
num1,num2 = map(float,input("enter a float number : ").split())
print("The addition of ",num1," and ",num2," results ",add(num1, num2),".")

def evenOdd(num):
	if (num % 2 == 0):
		print(num," is even")
	else:
		print(num," is odd")
print("A simple Python function to check whether number is even or odd")
num = float(input("enter a number to check even/odd : "))
evenOdd(num)

def MyFun(x, y=50): # y=50 is default arguement
    """function for default arguement where y is 50 """
    print("value of x is : ", x)
    print("value of y is : ", y)

print(MyFun.__doc__)
x = int(input("enter a number for x : "))
MyFun(x)

def myFun(**kwargs):
    """*kwargs for variable's number of keyword arguments"""
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
print(myFun.__doc__)
St,Sc,Sl = map(str, input("enter first mid last value with space ").split())
myFun(first=St, mid=Sc, last=Sl)

def sqr_value(num):
    """This function returns the square value of the entered number"""
    return num**2
print(sqr_value.__doc__)
a = int(input("enter a number to get sqrt of it : "))
print("sqrt of ",a,"is : ",sqr_value(a))