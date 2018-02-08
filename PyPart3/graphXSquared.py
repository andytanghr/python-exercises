import matplotlib.pyplot as plot

def xSquared(x):
  return x ** 2

xs = list(range(-100, 101))
ys = []
for x in xs:
  ys.append(xSquared(x))

plot.plot(xs, ys)
plot.show()
