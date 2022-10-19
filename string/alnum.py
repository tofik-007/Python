#isalnum,isalpha,islower,upper,isdigit,isspace
from unicodedata import digit

str = input("enter a string without space to check isalnum/isalpha function : ")  # No space in this string
print ("if input contains digits & alphabet it's alnum : ",str.isalnum()) #accepts digits & alphabet
print ("if input contains alphabet only it's isalpha : ",str.isalpha()) # accepts only alphabet

str2 = input("enter a string without space to check islower/isupper function : \n")
print("input is in lowercase only : ",str2.islower())
print("input is in Uppercase only : ",str2.isupper())

a = input("enter the digits  : \n")
print("input contains all digit : ",a.isdigit())   #isnumeric applies on unicode object doesn't support float

space = input("enter multiple spaces only to check isspace() :")
print("input contains only space ""__"" without any word/digit then it gives true :",space.isspace())
