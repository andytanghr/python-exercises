from turtle import *

def drawEquilateralTriangle(size=100, fill=False, hue='black'):
  color(hue)
  if fill == True:
    begin_fill()
    for line in range(3):
      right(120)
      forward(size)
    end_fill()
  else:
    for line in range(3):
      right(120)
      forward(size)

def drawSquare(size=100, fill=False, hue='black'):
  color(hue)
  if fill == True:
    begin_fill()
    for line in range(4):
      right(90)
      forward(size)
    end_fill()
  else:
    for line in range(4):
      right(90)
      forward(size)
      
def drawPentagon(size=100, fill=False, hue='black'):
  color(hue)
  if fill == True:
    begin_fill()
    for line in range(5):
      right(72)
      forward(size)
    end_fill()
  else:
    for line in range(5):
      right(72)
      forward(size)

def drawHexagon(size=100, fill=False, hue='black'):
  color(hue)
  if fill == True:
    begin_fill()
    for line in range(6):
      forward(size)
      right(60)
    end_fill()
  else:
    for line in range(6):
      forward(size)
      right(60)

def drawOctagon(size=100, fill=False, hue='black'):
  color(hue)
  if fill == True:
    begin_fill()
    for line in range(8):
      forward(size)
      right(45)
    end_fill()
  else:
    for line in range(8):
      forward(size)
      right(45)

def drawStar(size=100, fill=False, hue='black'):
  color(hue)
  #fillcolor(hue)
  if fill == True:
    begin_fill()
    for line in range(5):
      right(144)
      forward(100)
    end_fill()
  else:
    for line in range(5):
      right(144)
      forward(100)  

def drawCircle(size=100, fill=False, hue='black'):
  color(hue)
  if fill == True:
    begin_fill()
    circle(size)
    end_fill()
  else:
    circle(size)
      
      
        

# mainloop()