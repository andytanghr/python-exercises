from turtle import *

def drawOctagon():
  for line in range(8):
    forward(100)
    right(45)

if __name__ == '__main__':
  drawOctagon()
  mainloop()
