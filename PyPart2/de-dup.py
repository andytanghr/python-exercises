listWithDups = [-5, -4, -4, -1, -1, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listWithoutDups = []
for number in listWithDups:
    if listWithDups.count(number) == 1:
        listWithoutDups.append(number)
print(listWithoutDups)