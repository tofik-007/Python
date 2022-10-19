def Max():
    """function to get max in list"""
    List = list(map(int,input("enter value for list : ").split()))
    print("list is : ",List)
    print("maximum of list is : ",max(List))
print(Max.__doc__)
Max()
