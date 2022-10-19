#str method of upper lower title  & capitalize
str = input("enter a string : ")
print("title method to make 1st letter capital of every word in string : ",
      str.title())  # "str.title() makes 1st letter of every word capital : ",
print("capitalize method to make 1st letter of string - > capital : ",
      str.capitalize())  # "str.capitalize() to make 1st letter of string capital :"
# "str.upper() to convert whole string n capital"
print("upper method to convert whole string into capital :", str.upper())
# "str.lower() to convert whole string n lowewrcase"
print("upper method to convert whole string into lowercase :", str.lower())
x = input("enter a part of string for checking in & not in method in above string : ")
print(x, "is given in string : ", x in str)

