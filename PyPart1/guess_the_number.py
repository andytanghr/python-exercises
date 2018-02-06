import random

print('I\'m thinking of a number between 1 and 10.')
lives = 5
print('You have {} guesses left'.format(lives))
guess = int(input('What\'s the number? '))
secret = random.randint(1, 10)
# print(secret)
while guess != secret:
    if guess < secret:
        print('{} is too low.'.format(guess))
        print('You have {} guesses left'.format(lives))
    elif guess > secret:
        print('{} is too high.'.format(guess))
        print('You have {} guesses left'.format(lives))
    guess = int(input('What\'s the number? '))
    lives = lives - 1
    if lives == 0:
        print('You ran out of guesses!')
        break
    if guess == secret:
        print('Yes! You win!')
        again = input('Do you want to play again (Y or N)? ')
        if again == 'Y':
            lives = 5
            print('You have {} guesses left'.format(lives))
            guess = int(input('What\'s the number? '))
            secret = random.randint(1, 10)
        else:
            print('Bye!')
            break
    