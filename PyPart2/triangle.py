height = 4
width = 1
for row in range(height):
    print(' ' * height + '*' * width + ' ' * height)
    width += 2
    height -= 1
    