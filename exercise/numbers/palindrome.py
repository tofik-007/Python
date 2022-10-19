#program to check if number is palindrome or not
s = input("enter a string or number to check if it's palindrome or not ? ")
n = s[::-1]    #reverse the string
if s == n:
    print(s,"is palindrome.")
else:
    print(s,"is not palindrome.")
