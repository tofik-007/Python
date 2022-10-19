print("replace letter/word in string")
str = input("enter a string to perform the replace operations : ")
str1 = input("enter a word of string to replace it : ")
str2 = input("enter a word to use innstead of word presen in string : ")
print ("after replacement of ",str1,"with ",str2,", the string is : ",str.replace(str1, str2))
print("how many replacements ? ")
time = int(input("enter how many replacement you want : "))
print ("after",time,"replacement :",str.replace(str1, str2, time)) #2 shows , how many times replacement will take place

