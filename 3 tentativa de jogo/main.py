import pygame
from player import Player

# initializing
pygame.init()
display = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('uma tentativa de jogo')
clock = pygame.time.Clock()
gameLoop = True

# objetos
player = Player()
rect = pygame.rect.Rect(10, 10, 100, 100)
# game loop


def update():
    pass


def render():
    display.fill([10, 10, 10])

    pygame.draw.rect(display, [100, 100, 100], rect)

    pygame.display.update()


while gameLoop:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('jogo fechado')
            gameLoop = False
            break
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            rect.y -= 5
        if pressed_keys[pygame.K_s]:
            rect.y += 5
        if pressed_keys[pygame.K_a]:
            rect.x -= 5
        if pressed_keys[pygame.K_d]:
            rect.x += 5
    #
    update()
    render()
    clock.tick(120)
