import matplotlib.pyplot as plot

def convertCtoF(temperature):
  return temperature * 1.8 + 32

xs = list(range(-50, 50))
ys = []

for x in xs:
  ys.append(convertCtoF(x))

plot.plot(xs, ys)
plot.show()