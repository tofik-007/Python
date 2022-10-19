#startwith,endswith methods
str = input("enter a string : ")
s = input("enter a word to find weather the string starts with it or not : ")
print ("weather the string starts with ",s,"or not? ",str.startswith( s ))
print("if word is in any specific range , then give starting & ending point of str : ")
start = int(input("enter the starting index of string in which you want to check startwith method :"))
end = int(input("enter the ending index of string in which you want to check startwith method :"))
print ("startswith method check in ",start,"to",end ," :-> ",str.startswith( s, start, end ))  # sub,start,end
print("-----------------------------------------------------------------------------------------------------------------------------")
print("program to check endswith method.")
#check weather strings endswith given suffix or not. returns true/false
suffix = input("enter suffix to check weather above string endswith it or not ? ")
print ("string endswith suffix = ",suffix," :",str.endswith(suffix))
print("-----------------------------------------------------------------------------------------------------------------------------")
print("swapcase () method ")
print ("after swapcase : ",str.swapcase())
