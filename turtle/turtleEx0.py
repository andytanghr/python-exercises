from turtle import *

def drawSquare():
  forward(100)
  right(90)
  forward(100)
  right(90)
  forward(100)
  right(90)
  forward(100)

def drawCenteredSquare():
  # move into position
  up()
  forward(50)
  left(90)
  forward(50)
  left(90)

  down()

  # draw the square
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)

def drawCircleOnOrangeBkgd():
  pencolor('orange')
  width(10)
  circle(100)

def drawStar():
  for i in range(5):
    forward(100)
    right(144)

if __name__ == '__main__':
  shape('turtle')
  drawCircleOnOrangeBkgd()
  reset()
  drawSquare()
  reset()
  drawCenteredSquare()
  reset()
  drawStar()
  mainloop()