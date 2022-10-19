#tab expansion
txt = input("enter a sentance to to perform tab expansion  : ")
txt1 = txt[:5] + "\t" + txt[5:15] + "\t" + txt[15:25] + "\t" + txt[25:]
y = int(input("enter how many times you want to expand tab : "))
print ("exapanded tab: " +  txt1.expandtabs(y))