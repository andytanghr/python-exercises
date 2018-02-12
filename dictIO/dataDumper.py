import json

dataTest = {
  "data": [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
  ]
}

with open('dataTest.json', 'w') as fh:
  json.dump(dataTest, fh)
