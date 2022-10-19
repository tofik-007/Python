print("escape operator in python : ")
s = input("enter sentance to perform operation of escape operator in string :-> ")
print("backspace at index 1 : ",s[0]+"\b"+s[1:]) #backspace
s1 = s[:5] + "\t" + s[5:15] + "\t" + s[15:25] + "\t" + s[25:] 
print("tab : ",s1)                                                      #tab
print("vertical tab at index 10 : ",s[10] +"\v") #vertical tab (male sign)
print("formfeed at index 10 : ",s[10]+"\f") #formfeed (female sign)
print("new line from index 15 : ",s[:15]+"\n" + s[15:100]) #newline
print("shift letter at the end ",s[0:10]+"\r"+s[10:]) # shift letter at the end (carriage return)
#test
# s = 'lang\tver\nPython\t3'
# print(s)
# s1 = 'Ducati\tjaguar\npanigale\tf-type'
# print(s1)