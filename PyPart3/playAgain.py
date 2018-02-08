def playAgain():
  while True:
    answer = input('Do you want to play again (Y or N)? ')
    if answer.upper() == 'Y':
      return True
    elif answer.upper() == 'N':
      return False
    else:
      print('Invalid input')

if __name__ == '__main__':
  playAgain()