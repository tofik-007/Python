print("this splitlines fuction split the line from /n .")
txt = input("enter a sentance to split it in lines : ")
txt1 = txt[:5] + "\n" + txt[5:15] + "\n" + txt[15:25] + "\n" + txt[25:]
x1 = txt1.splitlines()
print("after splitline : ",x1)
print("with 'True' the splitlines is :")
print("with true to add 'n' too :",txt1.splitlines(True))
print("without 'True' the splitlines is :")
print("without the use of True is : ",txt1.split())
