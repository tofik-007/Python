print("dictionary method of getting value,key,items,has_key : ")
dict = {} #empty list

# number of elements as input
n = int(input("Enter number of elements in dict : "))

    # iterating till the range
for i in range(0, n):
    key = input("enter the key of dict :")
    ele = input("enter the value of dict :")
    dict[key]=ele # adding the element       
print("dict is : ",dict)
def value():
    """get value method : """
    print(value.__doc__)
    print("dictionary is : ",dict)
    print("values of dict is : ",dict.values())
def keys():
    """get keys method :"""
    print(keys.__doc__)
    print("dictionary is : ",dict)
    print("keys of dict is : ",dict.keys())
def items():
    """get items method : """
    print(items.__doc__)
    print("dictionary is : ",dict)
    print("dictionary item is : ",dict.items())
def has_key():
    """has_key mthod : """
    print(has_key.__doc__)
    print("has_key() method was removed in Python 3.")
value()
keys()
items()
has_key()