print("padding in string : - >")
str = input("enter a string to perform the padding operations : ")
print("entered input is : ", str)
width = int(input("enter a width which is to be padded in a string :"))
fill = input("enter a character for padding of string :")
print("length of string is : ",len(str))
print("padding at right side with ljust : ",
      str.ljust(width, fill))  # (width,fill_character)
print("padding at left side with rjust : ",
      str.rjust(width,fill)) #without character it filled with space # (width,fill_character)
print("zfill method of padding :",str.zfill(width))
# Python string method zfill() pads string on the left with zeros to fill width

