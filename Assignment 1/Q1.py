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
# SUM
sum = []
for col in range(column):
    temp = 0
    for row in range(rows):
        temp += matrix[row][col]
    sum.append(temp)
sum = tuple(sum)
print(sum)