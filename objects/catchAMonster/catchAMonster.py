import pygame
import random
import sys
import math

def main(level):
    WIDTH = 512
    HEIGHT = 480
    blue_color = (97, 159, 182)

    KEY_UP = 273
    KEY_RIGHT = 275
    KEY_DOWN = 274
    KEY_LEFT = 276

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    class Character():
        # def load(self, name):
        #     filename = 'images/' + name +'.png'
        #     image = pygame.image.load(filename)
        #     return image

        def draw(self, screen):
          screen.blit(self.image, (self.x, self.y))
        
        def __init__(self, name, x, y, xSpeed, ySpeed, image):
            self.name = name
            self.x = x
            self.y = y
            self.xSpeed = 5
            self.ySpeed = 5
            self.image = self.load(name)
            self.dead = False


        def move(self):
            #if name = hero, no screen wrapping
            self.x += self.xSpeed
            self.y += self.ySpeed

    class Hero(Character):
    #   def load(self, name):
        


        def __init__(self):
            self.hero = 'hero'
            self.x = 251 # initializes at center of field
            self.y = 235 # initializes at center of field
            self.xSpeed = 0
            self.ySpeed = 0
            self.dead = False
            self.image = pygame.image.load('images/hero.png').convert_alpha()

        def move(self, WIDTH, HEIGHT): #does hero take into arguments from keyboard input to move hero?
            # if hero at screen edge, stop motion
            padding = 70 # padding can be calibrated so that hero just barely touches it
            super(Hero, self).move()
            if self.x > WIDTH - padding:
                self.xSpeed = -3
            if self.y > HEIGHT - padding:
                self.ySpeed = -3
            if self.x < padding - 25: # check length 25 px
                self.xSpeed = 3
            if self.y < padding - 25:
                self.ySpeed = 3

    class Enemy(Character):
        def __init__(self):
            self.name = name
            self.x = x
            self.y = y
            self.xSpeed = 5
            self.ySpeed = 5
        
        def position(self, WIDTH, HEIGHT):
            # set direction
            # set distance/motion in loop, while true until random factor breaks? changes direction?
            # check position: if at screen edge, replace position on opposite edge, same direction
            # set random factor to change direction and distance
            self.x += self.xSpeed
            self.y += self.ySpeed
            if self.x > WIDTH:
                self.x = 0
            if self.y > HEIGHT:
                self.y = 0
            if self.x < 0:
                self.x = WIDTH
            if self.y < 0:
                self.y = HEIGHT

        def changeDirection (self, WIDTH, HEIGHT):
            direction = random.choice(['up', 'right', 'down', 'left'])
            if direction == 'up':
                self.up(WIDTH, HEIGHT)
            elif direction == 'right':
                self.right(WIDTH, HEIGHT)
            elif direction == 'down':
                self.down(WIDTH, HEIGHT)
            else:
                self.left(WIDTH, HEIGHT)

        def up(self, WIDTH, HEIGHT):
            self.xSpeed = 0
            self.ySpeed = -1
            self.position(WIDTH, HEIGHT)
        def right(self, WIDTH, HEIGHT):
            self.xSpeed = 1
            self.ySpeed = 0
            self.position(WIDTH, HEIGHT)
        def down(self, WIDTH, HEIGHT):
            self.xSpeed = 0
            self.ySpeed = 1
            self.position(WIDTH, HEIGHT)
        def left(self, WIDTH, HEIGHT):
            self.xSpeed = -1
            self.ySpeed = 0
            self.position(WIDTH, HEIGHT)
    
    class Monster(Enemy):
        # def load(self, name):
            

        def __init__(self, x, y):
            self.name = 'monster'
            self.x = x
            self.y = y
            self.dead = False
            self.image = pygame.image.load('images/monster.png').convert_alpha()
        
        # def move(self):
        #     pass


    class Goblin(Enemy):
        # def load(self, name):
        #     image = pygame.image.load(name)

      def __init__(self, x, y):
            self.name = 'goblin'
            self.x = x
            self.y = y
            self.dead = False
            self.image = pygame.image.load('images/goblin.png').convert_alpha()


    def checkCollision(char1, char2):
        # check if hero and monster positions collide
        # if true, win
        # check if hero and goblin positions collide
        # if true, lose
        distance = math.sqrt((char1.x - char2.x) ** 2 + (char1.y - char2.y) ** 2)
        if distance < 32: # all char images are 32px x 32 px
            char2.dead = True
            return True
        else:
            return False

    # when hero and monster collide, game is won and next level starts
    def win(newLevel, screen):
        pygame.mixer.music.load('sounds/win.wav')
        pygame.mixer.music.play()
        font = pygame.font.Font(None, 25) # change size 25 pt?
        text = font.render('You win! Hit ENTER to play again', True, (0, 0, 0))
        screen.blit(text, (113, 220)) # change coordinates to center more precisely
        pygame.display.update()
        wait()
        main(newLevel)
            
    # when hero and goblin collide, game is lost and level resets to zero
    def lose(screen):
        pygame.mixer.music.load('sounds/lose.wav')
        pygame.mixer.music.play()
        font = pygame.font.Font(None, 25)
        text = font.render('You lose! Hit ENTER to play again', True, (0, 0, 0))
        screen.blit(text, (113, 220)) # change coordinates to center more precisely
        pygame.display.update()
        wait()
        main(1) # resets to level 1

    # waits for user to press ENTER to continue to next level after win or reset game after loss
    def wait():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return 0

    # play game music
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1) # plays forever

    # initialize pygame framework
    pygame.init()

    # draw screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # set window caption
    pygame.display.set_caption('Catch A Monster!')

    # create a clock
    clock = pygame.time.Clock()

    # background image
    background = pygame.image.load('images/background.png').convert_alpha()

    # create loop counter to coordinate all enemy chars' change in direction
    loopCount = 0

    # initialize characters
    hero = Hero()
    monster = Monster(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    characters = [hero, monster]
    enemies = [monster]
    goblins = []
    numberGoblins = level + 2 # check amount
    for goblin in range(0, numberGoblins):
        newGoblin = Goblin(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
        characters.append(newGoblin)
        enemies.append(newGoblin)
        goblins.append(newGoblin)

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            # while user moves hero using arrow keys
            # when keys are not pressed
            if event.type == pygame.KEYUP:
                if event.key == KEY_UP:
                    hero.ySpeed = 0
                elif event.key == KEY_RIGHT:
                    hero.xSpeed = 0
                elif event.key == KEY_DOWN:
                    hero.ySpeed = 0
                elif event.key == KEY_LEFT:
                    hero.xSpeed = 0
            # when keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    hero.ySpeed = -3
                elif event.key == KEY_RIGHT:
                    hero.xSpeed = 3
                elif event.key == KEY_DOWN:
                    hero.ySpeed = 3
                elif event.key == KEY_LEFT:
                    hero.xSpeed = -3

                if event.type == pygame.QUIT:
                    stop_game = True

        # Game logic

        # Draw background
        screen.fill(blue_color)

        # update game state
        hero.move(WIDTH, HEIGHT)
        for char in enemies:
            if loopCount % 120 == 0:
                char.changeDirection(WIDTH, HEIGHT)
            else:
                char.position(WIDTH, HEIGHT)

        # check if hero and monster collide
        if checkCollision(hero, monster):
            win(level + 1, screen)
        
        # check if hero and a goblin collide
        for goblin in goblins:
            if checkCollision(hero, goblin):
                lose(screen)

        # Game display
        
        # show background
        screen.blit(background, [0, 0])

        # show current level
        font = pygame.font.Font(None, 25)
        text = font.render('Level ' + str(level), True, (255, 0, 0), (63, 134, 48))
        screen.blit(text, (32, 32))

        # draw each alive character every loop
        for char in characters:
            if not char.dead:
                char.draw(screen)
            else:
                pass
        
        # update drawn graphic frame
        pygame.display.update()

        # keep time
        clock.tick(60)

        # increase loop count by 1
        loopCount += 1

    # quit
    pygame.quit()

if __name__ == '__main__':
    main(1)
