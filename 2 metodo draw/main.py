import pygame
from math import radians

# initializing pyGame
pygame.init()
display = pygame.display.set_mode([500, 500])
pygame.display.set_caption('game test :)')
clock = pygame.time.Clock()
gameLoop = True
# objects
someRect = pygame.rect.Rect(10, 10, 100, 100)


# some variables

# metodos
def media(pontos: list):
    mX, mY = 0, 0
    for point in pontos:
        mX += point[0]
        mY += point[1]
    mX /= len(pontos)
    mY /= len(pontos)
    return [mX, mY]


# game loop
def update():
    someRect.x += 1


def render():
    display.fill([10, 10, 10])  # background
    pygame.draw.rect(display, [200, 200, 200], someRect)
    pygame.draw.line(display, [0, 200, 100], [0, 100], [someRect.x, someRect.y], 10)
    pygame.draw.arc(display, [200, 0, 0], someRect, radians(0), radians(90), 10)

    pygame.draw.circle(display, [100, 100, 250], [50, 150], 50, 5)

    polygon = [[0, 250], [250, 250], [250, 400]]
    pygame.draw.polygon(display, [200, 250, 200], polygon, 1)
    pygame.draw.circle(display, [200, 250, 200], media(polygon), 2)

    pygame.display.update()


while gameLoop:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('saindo do jogo')
            gameLoop = False
            break
    #
    update()
    render()
    clock.tick(60)
