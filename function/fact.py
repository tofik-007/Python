def fact(n):
    n_fact = 1
    for i in range( 1, n + 1 ):
        n_fact = n_fact * i
    return n_fact
n = int(input("enter a number to get it's factorial : " ))
print("factorial is : ",fact(n))