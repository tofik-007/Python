print("list to tuple conversion")
tuple = tuple(map(int, input("enter value of tuple : ").split()))
print(type(tuple))
print ("Tuple elements : ", tuple)
print("list is :",list(tuple))
print("unpacking of tuple")
games = ('nfs','gta','asphalt','most wanted')
( *like, want, love , desire) = games
print(like)
print(want)
print(love)
print(desire)