#subtraction of matrix
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

#another matrix

print("here wen used above dimensions for the matrix because different dimensions can't be use for operations : ")

matrix1 = []
print("Enter the entries row wise : ")

for i in range(r):         # A for loop for row 
	b =[]
	for j in range(c):	 # A for loop for column 
		b.append(int(input()))
	matrix1.append(b)

for i in range(r):
	for j in range(c):
		print(matrix1[i][j], end = " ")
	print()

matrix2 = [[0]*r for i in range(c)]

print("subtraction of matrix : ")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix2 [i] [j] = matrix[i][j] - matrix1[i][j]
for x in matrix2:
    print(x)