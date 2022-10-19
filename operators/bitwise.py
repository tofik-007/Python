a = 34 
b = 35
if a < b & a > b: #&
    print("if both conditions are right then this will print")
else:
    print("if anyone conditions is wrong then this will print ")

if a > b | a >= b: 
    print("if anyone conditions is right then this will print")
else:
    print("if both conditions are wrong then this will print")
print(a ^ b) #xor gate logic


print(~a ) #	Bitwise NOT =--> 1's compliment


print("binary left shift : ",a << b)  #binary left shift *
print(a << 1)  #binary left shift *
print(a >> 2)  #binary right shift /
print(a >> 1)  #binary right shift /
 
