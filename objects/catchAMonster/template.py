import pygame

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    def load(name):
        # name = 'monster'
        filename = 'images/' + name + '.png'
        image = pygame.image.load(filename).convert_alpha()



        # try:
        #     pygame.image.load(name)
        # except pygame.error, message:
        #     print('Cannot load image: {}'.format(name)) 
        #     raise SystemExit, message
        # self.image = self.load('images/monster.png')
    # load('monster')    


    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)

        # Game display
        load('monster')
        image.blit(image, (0, 0))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
