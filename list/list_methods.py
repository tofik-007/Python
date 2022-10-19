print("del,index,pop,remove,reverse in list")
l = list(map(int,input("enter value for list : ").split()))
print("list is : ",list)
def dEl():
    print("<<<<<<<<<<-----------delete the object of list ----------->>>>>>>>>>\n")
    print(list,"\n")
    dEl = int(input("enter index number of object you want to delete :"))
    del(list[dEl]) #delete the object
    print("index after deleting the object : ",list,"\n")
def index():
    print("<<<<<<<<<<----------- get index of object of list object ----------->>>>>>>>>>\n")
    print(list,"\n")
    ind = input("enter a object of which index you want : ")
    print("index of object '",ind,"' is",list.index(ind),"\n")
def pop():
    print("<<<<<<<<<<----------- removal of object & return it in list ----------->>>>>>>>>>\n")
    print(list,"\n")
    index = int(input("enter an index number of object which you want to remove & return in output : "))
    print(list.pop(index))
    print("after pop",index," list is --> ",list,"\n")
def rem():
    print("<<<<<<<<<<-----------remove object ----------->>>>>>>>>>\n")
    print(list,"\n")
    obj = input("enter an object to remove it from a list : ")
    list.remove(obj)
    print("after remove '",obj,"' list is --> ",list,"\n")
def reverse():
    print("<<<<<<<<<<----------- reverse the list ----------->>>>>>>>>>\n")
    print("original list is : ",list,"\n")
    list.reverse() #print nothing while in() of print
    print("reversed list is : ",list,"\n")
reverse()
dEl()
index()
pop()
rem()
