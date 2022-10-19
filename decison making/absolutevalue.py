# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1
num = int(input("enter a number :"))
# print(num*-1) if num < 0 else print("absolute value is",num)
if num < 0:
    print("absolute value is",num*-1)
else:
    print("absolute value is",num)