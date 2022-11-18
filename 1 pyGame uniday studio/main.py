import pygame
from blob import Blob
from bixin_b import Bixin

# initializing game
pygame.init()
display = pygame.display.set_mode([800, 400])
pygame.display.set_caption('meu game')

running = True
clock = pygame.time.Clock()
# music
# pygame.mixer.music.load('data/music/song18.mp3')
# pygame.mixer.music.play(-1)

# sounds
'''laser = [pygame.mixer.Sound('data/sounds/laser1.mp3'),
         pygame.mixer.Sound('data/sounds/laser5.mp3'),
         pygame.mixer.Sound('data/sounds/laser9.mp3')]'''

# objects
objGroup = pygame.sprite.Group()

player = Blob(objGroup)
bixin = Bixin(objGroup)

x = 0
y = 0
v = 10


# game loop


def render():
    display.fill([50, 50, 50])
    objGroup.draw(display)

    pygame.draw.rect(display, [200, 200, 200, 255],
                     pygame.Rect(x, y, 50, 50))

    pygame.display.update()


def update():
    objGroup.update()


while running:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pass
                # laser[0].play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pass
                # laser[2].play()
        # pressed keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            y -= v
        if pressed_keys[pygame.K_s]:
            y += v
        if pressed_keys[pygame.K_a]:
            x -= v
        if pressed_keys[pygame.K_d]:
            x += v

    render()
    update()
    clock.tick(120)
