#program for prime number
n = int(input("Enter a number to check if it's prime or not: "))
# If n is greater than 1
if n > 1:
   # Check if factor exist  
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
# Else if the input n is less than or equal to 1
else:
   print(n,"is not a prime number")