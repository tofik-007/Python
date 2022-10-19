print("this program will remove the letter of your choice from your given string with the use of continue.")
str = input("enter the string :")
print(str)
esc = input("enter the first letter you don't want to print from given string : ")
esc1 = input("enter the second letter you don't want to print from given string : ")
for letter in str:
    if letter== esc or letter == esc1:
        continue
    print(letter)