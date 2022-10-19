# # a file named "test", will be opened with the reading mode.
# file = open('test.txt', 'rb')
# # This will print every line one by one in the file
# for each in file:
# 	print (each)

# print()
# file = open('test.txt', 'r')
# # This will print every line one by one in the file
# for each in file:
# 	print (each)
# print()
# file = open('test.txt', 'r+')
# # This will print every line one by one in the file
# for each in file:
# 	print (each)
# print()
# file = open('test.txt', 'rb+')
# # This will print every line one by one in the file
# for each in file:
# 	print (each)

with open("test1.txt", "a+") as f:
    n = input("enter")
    f.write(n)

# with open("file1.txt", "w+") as f:
#     f.write("c")