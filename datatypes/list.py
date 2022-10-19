#basic list intro
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
list[1] = 124   #update the values
print(list.append("james"))
print (list)       # Prints complete list
print("updated list",list)
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[::-1])     #  slicing method   
print (list[2:])      # Prints elements starting from 3rd element
print (list[:3])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
# elements & size can be changed in list (mutable)






