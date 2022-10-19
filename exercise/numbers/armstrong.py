print("armstrong number : every digit's power(length) is equal to number it self ")
n = int(input("enter a mumber to check if it's a armstrong number or not? ")) 
s = n 
b = len(str(n)) #used 3 but didn't work for 4 digit numbers
sum = 0
while n != 0:
	r = n % 10 #remainder
	sum += (r**b) 
	n = n//10 #quotient
if s == sum :
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")
