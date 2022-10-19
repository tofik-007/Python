s = input("enter a string to count it's vowel and constant : ")
vowel,constant,space = 0,0,0
for i in s:
    if i == 'A' or i =="a" or i == "E" or i == "e" or i =="I" or i == "i" or i == "O" or i == "o" or i == "U" or i == "u":
        vowel += 1
    elif i == " ":
        space += 1
constant = len(s) - space - vowel
print("number of vowel in string is %d and constant is %d "%(vowel,constant))
