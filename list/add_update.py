print("add,update,insert method in list")
l = list(map(int, input("enter value of list : ").split()))
print("list is : ",l)

def add():
    print("<<<<<<<<<<----------- append the list ----------->>>>>>>>>>\n")
    print(l,"\n")
    add = input("add the object for list to apppend it : ")
    l.append( add ) #add at the end of l
    print ("appended list : ", l,"\n")

def update():
    print("<<<<<<<<<<----------- list update ----------->>>>>>>>>>\n")
    print(l,"\n")
    index = int(input("enter numbder of index which you want to update (digit): "))
    update  = input("enter new object to update it at the current object of index  : ")
    l [index] = update #update object
    print("updated list : ",l,"\n")
def insert():
    print("<<<<<<<<<<----------- insert object in list ----------->>>>>>>>>>\n")
    print(l,"\n")
    index = int(input("enter an index number at which you want to insert object (digit) :->"))
    val = input("enter a value for object to insert in the l : ")
    l.insert(index,val)
    print("after inserting ",val," at ",index," list is ",l,"\n")
add()
update()
insert()

