print("sorting of list")
def sort():
    print("<<<<<<<<<<----------- sort the list(create list to sort it) ----------->>>>>>>>>>\n")
    l = list(map(int, input("enter value of list : ").split()))
    print("list before sorting is : ",l,"\n")
    l.sort()
    print("list after sorting is : ",l,"\n")
sort()