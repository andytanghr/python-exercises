width = int(input('Width? '))
height = int(input('Height? '))

topBottom = '*' * width

print(topBottom)
for row in range(0, height-2):
    spaces = ' ' * (width-2)
    print('*' + spaces + '*')
print(topBottom)