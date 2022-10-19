'''program to check if a year is leap year or not If a year is divisible by 4 then it is leap 
year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 4'''
year = int(input("enter the year to check if it's leap or not : "))
if year % 4 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")