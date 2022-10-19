n = int(input("enter a number to check if it's prime or not ? "))
if n > 1:
    for i in range(2,n):
        if n % i == 0: #remainder
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")
