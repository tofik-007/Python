# matrix additions +

r = int(input("enter row : "))
c = int(input("enter column : "))

matrix = []
print("enter value for  matrix row wise : ")
for i in range(r):  # for row
    a = []
    for j in range(c):  # for column
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()

print("here wen used above dimensions for the matrix because different dimensions can't be use for operations : ")

matrix1 = []
print("enter value for  matrix row wise : ")
for i in range(r):
    b = []
    for j in range(c):
        b.append(int(input()))
    matrix1.append(b)
for i in range(r):
    for j in range(c):
        print(matrix1[i][j], end=" ")
    print()

matrix2 = [[0]*r for i in range(c)]

print("addition of matrix : ")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix2[i][j] = matrix[i][j] + matrix1[i][j]
for x in matrix2:
    print(x)

print("multipication of matrix : ")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix2[i][j] = matrix[i][j] * matrix1[i][j]
for x in matrix2:
    print(x)

print("division of matrix : ")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix2[i][j] = matrix[i][j] / matrix1[i][j]
for x in matrix2:
    print(x)
