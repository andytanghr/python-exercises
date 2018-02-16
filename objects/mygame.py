import pygame

pygame.init() #initializes graphics, sound, etc. aspects of library

screen = pygame.display.set_mode((500,500))

x = 0
y = 0

pygame.draw.rect(
  screen,
  (255, 0, 0)
  (200, 200, 100, 100),
  0
)

pygame.display.update()

while True: #must have event loop to keep display screen up
  for event in pygame.event.get():
    if event.type == pygane.QUIT: #this cataches the quit event that the program is waiting for upon click
      sys.exit()

