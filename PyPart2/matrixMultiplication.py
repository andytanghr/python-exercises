# matrixA = [[2, -2], [5, 3]]
# matrixB = [[-1, 4], [7, -6]]
# product = []
# line = []
# for rowA in range(0, len(matrixA)):
#     line[rowA] = []
#     for columnB in range(0, len(matrixA)):
#         element = 0
#         for rowB in range(0, len(matrixA)):
#             element = (matrixA[rowA][rowB] * matrixB[rowB][columnB])
#             line.append(element)
#     product.append(line)
# print(product)

matrixA = [[2, -2], [5, 3]]
matrixB = [[-1, 4], [7, -6]]
product = []
for row in range(len(matrixA)):
    product.append(row)
    for column in range(len(matrixB)):
        element = 0
        for width in range(len(matrixB)):
            element += matrixA[row][width] * matrixB[width][column]
        product[row][column].append(element)
print(product)