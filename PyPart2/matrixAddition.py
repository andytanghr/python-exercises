matrix1 = [[1, 3], [2, 4]]
matrix2 = [[5, 2], [1, 0]]
resultant = []
# need to use nested loops to traverse each list's element to add to corresponding of another list's element
# summation elements for every line of resultant is generated, then appended to resultant
# "line" is synonym to "row"
for row in range(0, len(matrix1)):
    line = []
    for column in range(0, len(matrix2)):
        line.append(matrix1[row][column] + matrix2[row][column])
    resultant.append(line)
print(resultant)