
def letter_histogram():
  word = input('Input word enclosed by quote marks to tally its characters: ')
  print(type(word))
  histogram = {}
  for char in word:
    if char not in histogram:
      histogram[char] = 1
    else:
      histogram[char] += 1
  # print(histogram)
  return histogram

if __name__ == '__main__':
  letter_histogram()




