def enumrate():
    """Write a program to create function func1() to accept a variable
    length of arguments and print their value."""
    l = list(map(str, input("enter a number of list via space between it : ").split()))
    for index, val in enumerate(l,start=1):
        print(index,"arguement is :",val)
print(enumrate.__doc__)
enumrate()