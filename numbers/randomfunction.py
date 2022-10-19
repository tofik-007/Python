#use of random function in py
import random
#05/09/2022
s = input("enter a string : \n")
print(random.choice(s))
# print("Select an even number in 100 <= number < 1000 random range") 
print ("randrange(100, 1000, 2) : ", random.randrange(100, 1000,2))
print ("generation of random number random() : ", random.random())
# print("reshuffle list")
# lst = [] #-->empty list

# # number of elements as input
# n = int(input("Enter number of elements : "))

# # iterating till the range
# for i in range(0, n):
# 	value = int(input())

# 	lst.append(value) # adding the element
	
# print(lst)
# random.shuffle(lst)
# print("Reshuffled list : ",  lst)
print("Random float (uniform)")
x = int(input("enter value of x :"))
y = int(input("enter value of y :"))
print ("random.uniform(x,y)--> random number between x , y  ",  random.uniform(x, y))

