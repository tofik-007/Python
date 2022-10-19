print("this will stop Printing letters of a sentance from 'a' and  'e' .")
i = 0
a = input("enter a sentance : ")

while i < len(a):
	if a[i] == 'e' or a[i] == 'a':
		i += 1                       
		break
	print("letter from the sentance :", a[i])
	i += 1
