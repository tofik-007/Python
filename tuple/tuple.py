#tuple methods
tuple = tuple(map(float, input("enter value for tuple : ").split()))
print("Tuple is : ", tuple)
index = int(input("enter an index number to get it value : "))
print("value of index number '",index,"' is : ",tuple[index])  # access value
# tuples r immutable
print("tuple has following methods : ")
print("cmp() does not work in python 3")
print("length of tuple is : ", len(tuple))
print("max of tuple is : ", max(tuple))
print("min of tuple is : ", min(tuple))
#del tuple
print("before deleting tuple : ", tuple)
del tuple
print("after delete tuple ", tuple)

Tuple = tuple(map(int, input("enter value for tuple : ").split()))
print("Tuple is : ", Tuple)
tuple1 = set(Tuple)
tuple2 = tuple(tuple1)
print("after removing duplicate value from the tuple : ",tuple2)
print("after removing duplicate value from the tuple : ",tuple2)