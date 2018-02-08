def playAgain():
  while True:
    answer = input('Do you want to play again (Y or N)? ')
  if answer == 'Y':
    return True
  elif answer == 'N':
    return False
  else:
    print('Invalid input')

if __name__ == '__main__':
  playAgain()