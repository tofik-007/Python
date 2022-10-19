#transpose of matrix
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))

matrix = []
print("Enter the entries row wise : ")
 
for i in range(r):         # A for loop for row 
	a =[]
	for j in range(c):	 # A for loop for column 
		a.append(int(input()))
	matrix.append(a)
for i in range(r):
	for j in range(c):
		print(matrix[i][j], end = " ")
	print()

#blank matrix

matrix1 = [[0] * r for i in range(c)]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix1[j][i] = matrix[i][j]
print(matrix1)
