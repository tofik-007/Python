fo = open("test.txt","r")
print("name of the file is :",fo.name)
print("the mode of file :",fo.mode)
read = fo.read(5)
print(read)
print("before close() :",fo.closed)
fo.close()
print("after close() :",fo.closed)
fo = open("testing.txt", "ab+")
i = input("enter line for file : ")
fo.write(i.encode()) #byte like object is required that's why
# Close opend file
fo.close()