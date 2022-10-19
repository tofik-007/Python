# outer function
def outer_fun(a, b):
    """function that will accept two parameters, a and b
an inner function inside an outer function calculate the addition of a and b
At last,an outer function will add 5 into addition and return it""" 
    # inner function
    def addition(a, b):
        return a + b
    add = addition(a, b)   # inner function from outer function
    print("final sum is ",add + 5 )    # add 5 to the result
print(outer_fun.__doc__)
a, b = map(int, input("enter two number seprated by space : ").split())
outer_fun(a,b)
