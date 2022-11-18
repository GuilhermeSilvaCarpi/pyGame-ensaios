import pygame

# initializing
pygame.init()
display = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('uma tentativa de jogo')
clock = pygame.time.Clock()
gameLoop = True
# game loop


def update():
    pass


def render():
    display.fill([10, 10, 10])
    pygame.display.update()


while gameLoop:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('jogo fechado')
            gameLoop = False
            break
    #
    update()
    render()
    clock.tick(120)
