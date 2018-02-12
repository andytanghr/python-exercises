# Using turtle graphics, orionNightSky.py generates the constellation Orion's outline connected with its seven main stars
# Float values are used to ensure precision of completing outline of two quadrilaterals in which one side of each is shared
# Circles are drawn with a systematic error of a given star's pixel radius in the position the star's centers and orientation of the turtle at the start of drawing a given circle. In another version, drawing centered circles would be preferred.
# source of sky map/star chart: https://www.iau.org/public/themes/constellations/

from shapes import *

bgcolor('black')
pencolor('white')

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
  
  # k star
  right(138.75)
  forward(367) # z star, return for orienting for next quadrilateral
  drawCircle(23, True, 'white')

  # b star
  left(117.12)
  forward(396)
  drawCircle(41, True, 'white')

  # complete second quadrilateral, end drawing
  left(109.42)
  forward(417)

drawOrion()