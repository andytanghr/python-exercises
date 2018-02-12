import matplotlib.pyplot as plot
import json

filename = input('Enter a filename: ')
with open(filename, 'r') as fileHandle:
  contents = json.load(fileHandle)
  
xs = []
ys = []
for i in contents['data']:
  xs.append(i[0])
  ys.append(i[1])

plot.plot(xs, ys)
plot.show()