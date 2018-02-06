import random

print('I\'m thinking of a number between 1 and 10.')
guess = int(input('What\'s the number? '))
secret = random.randint(1, 10)
print(secret)
while guess != secret:
    if guess < secret:
        print('{} is too low.'.format(guess))
    elif guess > secret:
        print('{} is too high.'.format(guess))
    guess = int(input('What\'s the number? '))    
print('Yes! You win!')