coins = 0
print('You have {} coins.'.format(coins))
wantCoin = input('Do you want another one? ')
while wantCoin == 'yes':
    coins = coins + 1
    if coins == 1:
        print('You have 1 coin.')
    else:
        print('You have {} coins.'.format(coins))
    wantCoin = input('Do you want another one? ')
print('Bye')
    
