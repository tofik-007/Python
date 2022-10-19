# initializing a (3 x 2) matrix.
matrix = [[1, 2], [2, 3], [3, 4]]

# initializing another (2 x 3) matrix to store the result.
transpose = [[0, 0, 0], [0, 0, 0]]

# iterating the rows and then columns of each row
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

print(transpose,end=" ")
