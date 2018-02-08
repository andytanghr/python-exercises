import matplotlib.pyplot as plot

def oddOrEven(x):
  if x % 2 != 0:
    return 1
  else:
    return -1

xs = list(range(-5, 6))
ys = []

for x in xs:
  ys.append(oddOrEven(x))

plot.bar(xs, ys)
plot.show()