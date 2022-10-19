def calculation(a,b):
    """sum and subtraction of two numbers"""
    add,sub = a + b,a-b
    print("sum is :",add,"\nsubtraction is :", sub) 
print(calculation.__doc__)
a, b = map(int, input("enter two number seprated by space : ").split())
calculation(a,b)


