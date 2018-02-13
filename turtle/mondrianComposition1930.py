# A turtle graphics rendering of Piet Mondrian's 1930 painting, Composition with Red, Blue, and Yellow.

from shapes import *

setup(width=568, height=568)
bgcolor('white')
#speed(1)

def drawBlue():
  penup()
  setpos(-155,-135)
  pendown()
  blue = '#015d9e'
  drawSquare(140, True, blue)

def drawYellow():
  penup()
  setpos(284,-217)
  pendown()
  yellow = '#eedc6d'
  drawSquare(43, True, yellow)
  setpos(284,-232)
  drawSquare(43, True, yellow)

def drawRed():
  penup()
  setpos(284, 284)
  pendown()
  red = '#e02b25'
  drawSquare(435, True, red)

def drawThicker():
  penup()
  setpos(-284,105)
  setheading(0)
  pencolor('black')
  pendown()
  pensize(36)
  forward(120)

def drawLongestVertical():
  penup()
  setpos(-155, 280)
  setheading(270)
  pencolor('black')
  pendown()
  pensize(18)
  forward(564)

def drawLongestHorizontal():
  penup()
  setpos(-284, -144)
  setheading(0)
  pencolor('black')
  pendown()
  pensize(18)
  forward(584)

def drawShorters():
  # vertical 
  penup()
  setpos(232,-144)
  setheading(270)
  pencolor('black')
  pendown()
  pensize(18)
  forward(208)

  # horizontal
  penup()
  setpos(232,-217)
  setheading(0)
  pencolor('black')
  pendown()
  pensize(18)
  forward(43)


drawBlue()
drawYellow()
drawRed()
drawThicker()
drawLongestVertical()
drawLongestHorizontal()
drawShorters()
hideturtle()

mainloop()