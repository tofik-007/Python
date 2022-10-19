print("anonymous function with lambda : ")
#with lambda keyword
sum = lambda arg1, arg2: arg1 + arg2   # anonymous function
sum1 = lambda arg1, arg2: arg1 - arg2   # anonymous function
sum2 = lambda arg1, arg2: arg1 * arg2   # anonymous function
sum3 = lambda arg1, arg2: arg1 / arg2   # anonymous function
#call sum as a function
n1 , n2 = map(int, input("enter two number with space : ").split())
print ("Value of addition : ", sum( n1, n2 ))
print ("Value of subtraction : ", sum1( n1, n2 ))
print ("Value of multipication : ", sum2( n1, n2 ))
print ("Value of division : ", sum3( n1, n2 ))
