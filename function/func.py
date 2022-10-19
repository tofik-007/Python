# 
def info(name,age):
    """Write a program to create a function that takes two arguments, name and age, and print their value."""
    print("name : ",name,"\nage : ",age)
print(info.__doc__)
name = input("enter a name : ")
age = input("enter an age : ")
info(name,age)