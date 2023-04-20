import pygame
from triangle import Triangle
"""from math import sin, radians, degrees, dist
from mpmath import csc"""

# Initializing pygame
pygame.init()
display = pygame.display.set_mode([600, 600])
pygame.display.set_caption('testing triangles')
clock = pygame.time.Clock()
gameLoop = True

# Initializing objects
tri = Triangle([[100, 100], [400, 200], [300, 500]])
tri.color = [100, 200, 200]

point = [300, 200]
up: False
left: False
right: False
down: False


# Game loop
def update():
    tri.update()
    # Move point
    if up:
        point[1] -= 1
    if right:
        point[0] += 1
    if left:
        point[0] -= 1
    if down:
        point[1] += 1


def render():
    display.fill((50, 50, 50))  # Background

    tri.render(display)
    if tri.pointInside(point):
        pygame.draw.circle(display, [100, 200, 100], point, 20, 2)
    else:
        pygame.draw.circle(display, [200, 100, 100], point, 20, 2)
    pygame.draw.circle(display, [190, 190, 190], point, 2)

    pygame.display.update()  # Display update


while gameLoop:
    # Inputs
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            gameLoop = False
            break

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP]:
            up = True
        else:
            up = False
        if pressed_keys[pygame.K_RIGHT]:
            right = True
        else:
            right = False
        if pressed_keys[pygame.K_LEFT]:
            left = True
        else:
            left = False
        if pressed_keys[pygame.K_DOWN]:
            down = True
        else:
            down = False
    # Loop methods
    clock.tick(60)
    update()
    render()
