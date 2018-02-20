# 1 demonstrate Collatz conjecture
def showCollatz():
  n = int(input('Enter a number.. '))
  while n != 1:
    if n % 2 == 0:
      n = n / 2
      print(n)
    else:
      n = n * 3 + 1
      print(n)
# showCollatz()

# 2 find largest palindrome that is a product of two three-digit integers
def findLargestPalindrome(minimum, maximum):
  largestPalindrome = 900009 # smallest six-digit palindrome is 900009
  temp = 0
  for i in range(min, max):
    for j in range(min, max):
      temp  = i * j
      if isPalindrome(temp) and temp > largestPalindrome:
        largestPalindrome = temp
  return largestPalindrome
    
def isPalindrome(number):
  stringedNumber = str(number)
  reversedNumber = stringedNumber[::-1]
  if stringedNumber == reversedNumber:
    return True

min = 100
max = 1000
# print(findLargestPalindrome(min, max)) # 906609

# 3: find smallest number divisible by factors 1 to 20
def findSmallestDivisibleBy1To20():
  factor = 1
  largestFactor = 20
  number = largestFactor

  while True:
    if number % factor != 0: # if not div by factor
      number += largestFactor
      # print(number)
      factor = 1
      
    elif number % factor == 0: # if div by factor, check next factor
      factor += 1
    # print(factor)
    if factor == largestFactor and number % factor == 0:
      return number # 232792560

#   factor = 1
#   largestFactor = 20
#   number = 1
#   while True:
#     if number % factor == 0:
#       factor += 1
#     elif number % factor != 0:
#       number += 1

#     if factor == largestFactor and number % factor == 0::
#       return number

# print(findSmallestDivisibleBy1To20())

# 4: design a parking lot
