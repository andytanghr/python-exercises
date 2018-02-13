# A turtle graphics rendering of Piet Mondrian's 1930 painting, Composition with Red, Blue, and Yellow.
# Version 2 is to functionalize the squares, renders rectangles natively, corrects white space padding
from shapes import *

setup(width=580, height=580)
bgcolor('white')
#speed(1)

# draw blue
penup()
setpos(-155,-135)
pendown()
blue = '#015d9e'
drawSquare(140, True, blue)

# draw yellow
penup()
setpos(284,-217)
pendown()
yellow = '#eedc6d'
drawSquare(43, True, yellow)
setpos(284,-232)
drawSquare(43, True, yellow)

# draw red
penup()
setpos(284, 284)
pendown()
red = '#e02b25'
drawSquare(437, True, red)

# draw thicker line
penup()
setpos(-284,105)
setheading(0)
pencolor('black')
pendown()
pensize(36)
forward(120)

# draw longest vertical thinner line
penup()
setpos(-155, 275)
setheading(270)
pencolor('black')
pendown()
pensize(18)
forward(559)

# draw longest horizontal thinner line
penup()
setpos(-284, -135)
setheading(0)
pencolor('black')
pendown()
pensize(18)
forward(584)

# draw shorter thinner lines
# vertical 
penup()
setpos(232,-141)
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

mainloop()




#drawThinLine()