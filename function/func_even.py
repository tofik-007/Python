def even():
    """program to Generate even numbers between given numbers ."""
    s ,e = map(int, input("enter two numbers with space to to get even numbers in between : ").split())
    print("list of even numbers from",s,"to",e,"is : \n",list(range(s,e,2)))
    # print(" \ntuple : ",tuple(range(s,e,2)))
    # print("\nset : ",set(range(s,e,2)))
print(even.__doc__)
even()