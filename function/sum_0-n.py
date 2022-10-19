def sum(n):
    """WAP to create a recursive function to calculate the sum of numbers from 0 to entered number."""
    if n>=0:
        return n + sum(n-1)
    else:
        return 0
print(sum.__doc__)
n = int(input("enter a number to get the sum of 0 to that number : "))
print("sum of 0 to",n,"is : ",sum(n))