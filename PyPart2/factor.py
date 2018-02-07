factorMe = int(input('What number to factorize? '))
for factor in range(1, factorMe+1):
  if factorMe % factor == 0:
    print(factor)
    print(-factor)
