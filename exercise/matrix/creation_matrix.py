#creation of matrix
r = int(input("enter row number : "))
c = int(input("enter column number : "))

matrix = []
print("enter value row wise : ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()

#another matrix

ro = int(input("enter row number : "))
co = int(input("enter column number : "))

matrix1 = []
print("enter value row wise : ")
for i in range(ro):
    a = []
    for j in range(co):
        a.append(int(input()))
    matrix1.append(a)
for i in range(ro):
    for j in range(co):
        print("matrix : ",matrix1[i][j],end=" ")
    print()
