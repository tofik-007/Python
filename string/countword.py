print("prints the counts of the word in main str")
str = input("enter a main string :")
sub = input("enter a word to count :")
print("number of ", sub, " is : ", str.count(sub))
print("wanna find word in specific range ? ")
start = int(input("enter a starting point to find from above string :"))
end = int(input("enter a ending point to find from string :"))
print("from index ", start, "to", end, "number of", sub, "is : ",
      str.count(sub, start, end))  # 4 suggest the starting point of index4
