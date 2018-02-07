matrixA = [[2, -2], [5, 3], [1, 3]]
matrixB = [[-1, 4], [7, -6]]
product = []
for row in range(len(matrixA)):
    line = []
    for column in range(len(matrixB)):
        element = 0
        for width in range(len(matrixB)):
            element += matrixA[row][width] * matrixB[width][column]
        line.append(element)
    product.append(line)
print(product)