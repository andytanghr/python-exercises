import random

target = int(input('Enter a number between 0 and 100 for the computer to guess: '))
attempts = 1

# v1: computer guesses incrementally from 0 to 100:
# for guess in range(0, 101):
#   print('Guess #{}: {}'.format(guess, guess))
#   if guess == target:
#     print('The computer guessed correctly after {} tries.'.format(guess))
#     break
#   elif guess > target:
#     print('The computer guessed too high.')
#   else:
#     print('The computer guessed too low.')

# v2: computer guesses randomly
# while True:
#   guess = random.randint(0, 100)
#   print('Guess #{0}: {1}'.format(attempts, guess))
#   if guess == target:
#     print('The computer guessed correctly after {} tries.'.format(attempts))
#     break
#   elif guess > target:
#     print('The computer guessed too high.')
#     attempts += 1
#   else:
#     print('The computer guessed too low.')
#     attempts += 1


# v3: computer guesses by binary search
guess = random.randint(0, 100)
high = 100
low = 0
while True:
  print('Guess #{}: {}'.format(attempts,guess))
  if guess == target:
    print('The computer guessed correctly after {} tries.'.format(attempts))
    break
  elif guess > target:
    print('The computer guessed too high.')
    attempts += 1
    high = guess
    guess = random.randint(low, high)
  else:
    print('The computer guessed too low.')
    attempts += 1
    low = guess
    guess = random.randint(low, high)