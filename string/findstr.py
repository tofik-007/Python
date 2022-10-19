print("find.string = > find index of sub string in main string ")
str1 = input("enter main string : ")
str2 = input("enter sub string to find it in a main string : ")
print("length of main string is : ",len(str1))
print ("sub-string found in main string at index => ",str1.find(str2))
print("to find substring in specific range only :")
start = int(input("enter a starting point to find from above string :"))
end = int(input("enter a ending point to find from string :"))
print ("substring is in between inddex ",start," to ",end," => ",str1.find(str2, start,end)) #str, beg ,end
#index if found -1 else.