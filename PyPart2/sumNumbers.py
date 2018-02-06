listOfNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumOfList = 55

sum = 0
for number in listOfNums:
    sum += number
print(sum)
if sumOfList == sum:
    print('pass')

listOfOtherNums = [0, 2, 4, 6, 8, 10, 12]
sumOfOtherList = 42
sum = 0
for number in listOfOtherNums:
    sum += number
print(sum)
if sumOfList == sum:
    print('pass')