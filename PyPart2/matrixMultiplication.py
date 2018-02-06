matrixA = [[2, -2], [5, 3]]
matrixB = [[-1, 4], [7, -6]]
product = []

for row in range(0, len(matrixA)):
    line = []
    for column in range(0, len(matrixA)):
        for element in range(0, len(matrixA)):
            line.append(matrixA[row][element] * matrixB[element][column])
    product.append(line)
print(product)