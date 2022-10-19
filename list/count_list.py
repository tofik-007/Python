print("count & concate in the list")
list = list(map(int, input("enter value for list : ").split()))
print("list is : ",list)
def concate():
    print("<<<<<<<<<<-----------list concatenation ----------->>>>>>>>>>\n")
    print(list,"\n")
    print("now create sub list to concate it with main list : ")
    list2 = []
    n = int(input("Enter number of elements for list : "))
    for i in range(0, n):
        ele = input("enter the elements of list :")
        list.append(ele)  # adding the element
    # list2.extend(list)  #list+list2 ||| print(list2.extend(list)) --> none ?
    # print("sub list after extended with a main list : \n ",list2)
    print("concatenated list :",list + list2,"\n")
concate()
Count = input("enter a object to count it in above list : ")
print("count of object '",Count ,"' is ",list.count(Count),"times in list \n") #count 