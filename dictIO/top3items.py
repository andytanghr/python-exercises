# given a dictionary of item tallies, return max three times to get top 3-counted items

def top3items(tally):
  # tally = input('Enter a histogram tally to determine its top 3 items: ')
  top3 = []
  keys = list(tally.keys())
  values = list(tally.values())
  print(keys)
  print(values)


  for i in range(3):
    currentMaxIndex = values.index(max(values))
    # print(currentMaxKey)
    currentMax = keys[currentMaxIndex]
    top3.append(currentMax)
    keys.remove(currentMax)
    values.remove(values[currentMaxIndex])
  print(top3)
  return(top3)

top3items({'a':2, 'b':5, 'c':4, 'd':9, 'e':1})