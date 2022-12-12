import pygame
from player import Player
from time import time

# initializing
pygame.init()
display = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('an attempt at a game')
clock = pygame.time.Clock()
gameLoop = True
finalTime = time()
# game variables
buttons = [False, False, False, False]
# objects
player = Player(display)
# game loop


def update():
    player.update(deltaTime, buttons)


def render():
    display.fill([10, 10, 10])

    player.render()

    pygame.display.update()


while gameLoop:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('game finished')
            gameLoop = False
            break
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            buttons[0] = True
        else:
            buttons[0] = False
        if pressed_keys[pygame.K_a]:
            buttons[1] = True
        else:
            buttons[1] = False
        if pressed_keys[pygame.K_s]:
            buttons[2] = True
        else:
            buttons[2] = False
        if pressed_keys[pygame.K_d]:
            buttons[3] = True
        else:
            buttons[3] = False
    # loop
    initialTime = finalTime
    finalTime = time()
    deltaTime = finalTime - initialTime

    update()
    render()
    clock.tick(60)
