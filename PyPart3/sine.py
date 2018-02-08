import matplotlib.pyplot as plot
import math

def sine(x):
  return math.sin(x)

xs = list(range(-5, 6))
ys= []

for x in xs:
  ys.append(sine(x))

plot.plot(xs, ys)
plot.show()
