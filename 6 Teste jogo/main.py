import pygame
from player import Player
from enemy import Enemy

# Initializing
pygame.init()
display = pygame.display.set_mode([1000, 500])
isRunning = True
clock = pygame.time.Clock()

# Initializing objects
player = Player()
entities = [
    Enemy()
]


# Loop
def update():
    player.frameUpdate()
    for ent in entities:
        ent.frameUpdate(player)


def render():
    display.fill([20, 20, 20])

    player.render(display)
    for ent in entities:
        ent.render(display)

    pygame.display.update()


while isRunning:
    # Inputs
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
            break
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_q]:
        player.commands['item 1'] = True
    else:
        player.commands['item 1'] = False
    if pressedKeys[pygame.K_e]:
        player.commands['item 2'] = True
    else:
        player.commands['item 2'] = False
    if pressedKeys[pygame.K_UP] or pressedKeys[pygame.K_w]:
        player.commands['up'] = True
    else:
        player.commands['up'] = False
    if pressedKeys[pygame.K_LEFT] or pressedKeys[pygame.K_a]:
        player.commands['left'] = True
    else:
        player.commands['left'] = False
    if pressedKeys[pygame.K_DOWN] or pressedKeys[pygame.K_s]:
        player.commands['down'] = True
    else:
        player.commands['down'] = False
    if pressedKeys[pygame.K_RIGHT] or pressedKeys[pygame.K_d]:
        player.commands['right'] = True
    else:
        player.commands['right'] = False

    # Loop
    clock.tick(60)
    update()
    render()
