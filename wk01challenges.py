import math

def isPrime(n):
    if math.factorial(n-1) % n == -1 % n:
        return True
    else:
        return False 


#1.  FizzBuzz
def printFizzBuzz(length):
  for i in range(length + 1):
    if i % 15 == 0:
      print("FizzBuzz")
    elif i % 5 == 0:
      print("Buzz")
    elif i % 3 == 0:
      print("Fizz")
    else:
      print(i)

    
#2. Algo2
def findMultiples(length):
  sum = 0
  for i in range(length):
    if i % 5 == 0:
      sum += i
    elif i % 3 == 0:
      sum += i
  # print(sum)
  return sum

#findMultiples(1000) # 233168


#3. Algo3
def fibonacci(limit):
  sum = 0
  nPrev = 1
  n = 1
  while n < limit:
    if n % 2 == 0:
      sum += n
    print(n)
    temp = nPrev + n
    nPrev = n
    n = temp
    
  return sum

print('The sum of even-valued Fibonacci terms below four million is: {}'.format(fibonacci(4000000))) # 4613732
  

#4 Algo 4
def findLargestPrimeFactor(number):
  largestPrime = 2  
  # I'm sure there is some theorem that suggests looking for prime factors are necessarily small for some condition.
  # If such a theorem exists, then we can add another test for the loop index's value and stop the loop
  for i in range(2, number):
    if isPrime(i) and number % i == 0:
      largestPrime = i
      print(largestPrime)
  # print(largestPrime)
  return largestPrime

print('The largest prime factor of 600851475143 is: {}'.format(findLargestPrimeFactor(600851475143))) # >= 6857


#5. Finding the Nth Prime
def findNthPrime(n):
    primeToTest = 5
    primes = [2, 3]
    if n < 1:
      return 'n must be greater than 0'
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        while len(primes) < n: 
            if isPrime(primeToTest) == True:
                primes.append(primeToTest)
            primeToTest += 2 # twin prime conjecture to improve O(n) to O(n/2) but still linear O
    return primes[-1]

# print(findNthPrime(10001)) # 104743