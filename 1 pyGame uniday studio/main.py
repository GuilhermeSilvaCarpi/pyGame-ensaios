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
pygame.mixer.music.load('data/music/song18.mp3')
pygame.mixer.music.play(-1)

# sounds
laser = [pygame.mixer.Sound('data/sounds/laser1.mp3'),
         pygame.mixer.Sound('data/sounds/laser5.mp3'),
         pygame.mixer.Sound('data/sounds/laser9.mp3')]

# objects
objGroup = pygame.sprite.Group()

player = Blob(objGroup)
bixins = [Bixin(objGroup), Bixin(objGroup)]
bixins[0].rect.y += 120
bixins[0].rect.x += 200


# game loop
def render():
    display.fill([50, 50, 50])
    objGroup.draw(display)

    pygame.draw.rect(display, [200, 200, 200, 255],
                     pygame.Rect(10, 10, 50, 50))

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
                laser[0].play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                laser[2].play()
        # pressed keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            pass
        if pressed_keys[pygame.K_s]:
            pass
        if pressed_keys[pygame.K_a]:
            pass
        if pressed_keys[pygame.K_d]:
            pass

    render()
    update()
    clock.tick(120)
