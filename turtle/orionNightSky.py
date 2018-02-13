# Using turtle graphics, orionNightSky.py generates the constellation Orion's outline connected with its seven main stars.
# Turtle traces one path without overlap to draw all seven stars, in a figure eight.
# Float values are used to ensure precision of completing outline of two quadrilaterals in which one side of each is shared.
# Circles are drawn centered along the drawn path.
# The drawing is in the point of view as if observing the constellation perpendicular to the ecliptic.
# Source of sky map/star chart: https://www.iau.org/public/themes/constellations/

from shapes import *

setup(width=1080, height=1080)
bgcolor('black')
pencolor('white')
speed(8)
home()
angleCorrection = 36.64
left(angleCorrection) # angle correction after each home() reset, to display constellation as if observed perpendicular to the ecliptic

def drawOrion():
  # z star
  drawCircle(26.5, True, 'white')
  
  # e star
  forward(63.5)
  drawCircle(25, True, 'white')
  
  # d star
  forward(63.5)
  drawCircle(22, True, 'white')
  
  # g star
  left(39.28)
  forward(318)
  drawCircle(26.7, True, 'white')

  # a star
  left(97.48)
  forward(347)
  drawCircle(40, True, 'white')
  
  # z star reorientation
  left(118.6)
  forward(461)
  # drawCircle(26.5, False, 'white') # to test if the orientation of turtle matters for drawing circles. If perfect overlap of earlier z star, then it doesn't matter
  
  home() # resets orientation 
  left(angleCorrection) 

  # k star
  right(138.75)
  forward(367) # z star, return for orienting for next quadrilateral
  drawCircle(23, True, 'white')

  # b star
  left(117.12)
  forward(396)
  drawCircle(41, True, 'white')

  # complete second quadrilateral, end drawing
  left(109.42-2.5)
  forward(410)

  mainloop()

drawOrion()