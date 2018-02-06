# matrix1 = [[1, 3], [2, 4]]
# matrix2 = [[5, 2], [1, 0]]
resultant = []
matrix1 = [[2, 4], [7, 0], [6, 3]]
matrix2 = [[3, 1], [-1, 8], [-3, 3]]
# need to use nested loops to traverse each list's element to add to corresponding of another list's element
# summation elements for every line of resultant is generated, then appended to resultant
# "line" is synonym to "row"
# solution should work for any pair of matrices of same size
for row in range(0, len(matrix1)):
    line = []
    for column in range(0, len(matrix1[row])):
        line.append(matrix1[row][column] + matrix2[row][column])
    resultant.append(line)
print(resultant)