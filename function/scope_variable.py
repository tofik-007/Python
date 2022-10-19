print("scope of variable ")
a = 5 
def main():
    a = 4
    print("local variable : ",a)
    print("local variable's id : ",id(a))
print("a before function : ",a)    
main()
print("global variable : ",a)
print("global variable's id : ",id(a))