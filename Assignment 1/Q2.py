matrix = []
rows = int(input('Enter the number of rows '))
column = int(input('Enter the number of colums '))
# MAKING THE MATRIX
for row in range(rows):
    temp = []
    for col in range(column):
        temp.append(int(input('Enter the element ')))
    matrix.append(temp)
# PRINTING THE MATRIX
for row in matrix:
    print(row)
print('\n')
# TAKING THE TRANSPOSE
new = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in new:
    print(row)