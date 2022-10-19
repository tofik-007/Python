print("dict basics")
dict = {} #empty dict
# number of elements as input
n = int(input("Enter number of elements in dict : "))
# iterating till the range
for i in range(0, n):
    key = input("enter the key of dict :")
    ele = input("enter the value of dict :")
    dict[key]=ele # adding the element
print("dict is : ",dict)
print("length of dict : ",len(dict))
print("type of dict : ",type(dict))
print("str(dict) :-> produces a printable string representation of a dictionary : ",str(dict))
print("add in dict : ")
Add = input("enter a key for adding it to the dictionry : ")
Val = input("enter value to update : ") 
dict[Add] = Val #add/update
print("after add, dict is : ",dict) 
print("access dict items ")
a = input("enter the key to get it's value : ")
print("value of key '",a,"' is ",dict[a])
print("delete dict")
Del = input("enter a key to dlt it : ")
del dict[Del] #delete entry 
print("after deleting the entry with key ",Del," : ",dict)
dict.clear()
print("after clearing the dict : ",dict)
del dict
print("after deleting the whole dict : ",dict)
