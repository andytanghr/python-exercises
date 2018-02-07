import random

target = int(input('Enter a number between 0 and 100 for the computer to guess: '))
guessed = False
guesses = []
# v1: computer guesses incrementally from 0 to 100:
for guess in range(0, 101):
  print('Guess #{}: {}'.format(guess, guess))
  if guess == target:
    print('The computer guessed correctly after {} tries.'.format(guess))
    break
  elif guess > target:
    print('The computer guessed too high.')
  else:
    print('The computer guessed too low.')
# v2: computer guesses randomly
while guessed != True:
  guess = random.randint(0, 100)
  print('Guess #{}: {}'.format(guess, guess))
  if guess == target:
    print('The computer guessed correctly after {} tries.'.format(guess))
    guessed = True
    break
  elif guess > target:
    print('The computer guessed too high.')
  else:
    print('The computer guessed too low.')


# v3: computer guesses 50 first, then goes
# v4: computer divides and conquers by binary guess
# while guessed != True:
#   guess = random.randint(0, 100)
#   if guess == target:
