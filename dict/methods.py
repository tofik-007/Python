print("dict methods of copy,get,update,setdefault,fromkey : ")
dict = {} #empty list
# number of elements as input
n = int(input("Enter number of elements in dict : "))
    # iterating till the range
for i in range(0, n):
    key = input("enter the key of dict :")
    ele = input("enter the value of dict :")
    dict[key]=ele # adding the element       
print("dict is : ",dict)
def copy():
    """copy method to copy one dict to another """
    print(copy.__doc__)
    print("main dictionary is : ",dict)
    dict1 = dict.copy()
    print("copied dict in dict 1 is : ",dict1)
def get():
    """get method to get value of key (key if exist else none ): """
    print(get.__doc__)
    print("dictionary is : ",dict)
    key = input("enter a key to get it value from dictionary : ")
    print("value of ",key," is : ",dict.get(key)) #get method :-> print(dict[key])
def setdefault():
    """set default method (key if exist else ' default value for key ' ) """
    print(setdefault.__doc__)
    print("dictionary is : ",dict)
    Key = input("enter a key to get it value from dictionary : ")
    print("key exist in dict : ",dict.setdefault(Key,"error"))
def update():
    """update method of dict """
    print(update.__doc__)
    dict1 = {} #empty dict
    # number of elements as input
    n = int(input("Enter number of elements in dict : "))
    # iterating till the range
    for i in range(0, n):
        key = input("enter the key of dict :")
        ele = input("enter the value of dict :")
        dict1[key]=ele # adding the element       
    print("dict1 is : ",dict1)
    dict.update(dict1)
    print("main dict is : ",dict)
def fromkey():
    print(fromkey.__doc__)
    print("main dictionary is : ",dict)
    default = input("enter a default value : ")
    dict2 = dict.fromkeys(dict,default)
    print("dictionary 2 having keys of main dictionary : ",dict2)
# copy()
# get()
# setdefault()
update()
# fromkey()
