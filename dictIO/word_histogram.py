# this assumes only alphanumeric characters, no punctuation or special characters
def word_histogram():
  text = input('Enter text to count word frequency: ')
  tempWord = ''
  #wordList = []
  histogram = {}
  
  # extract characters into words
  for char in range(len(text)):
    if text[char].isalpha():
      tempWord += text[char]
    elif text[char] == ' ' or char == len(text):
      if tempWord not in histogram:
        histogram[tempWord] = 1
      else:
        histogram[tempWord] += 1
      tempWord = ''

  print(histogram)
  return histogram

  if __name__ == '__main__':
    word_histogram()









if __name__ == '__main__':
  word_histogram()