# Take two int values from user and print greatest among them.
a = float(input("enter a number : "))
b = float(input("enter a number : "))
if a > b:
    print(a,"is greater than ",b)
elif a < b:
    print(b,"is greater than ",a)
else: 
    print("both are equal")