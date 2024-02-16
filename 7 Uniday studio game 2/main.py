import pygame
from player import Player
from asteroid import Asteroid
from random import randint
from plasma import Plasma

# initializing game
pygame.init()
display = pygame.display.set_mode([800, 400])
pygame.display.set_caption('asteroidos')
pygame.display.set_icon(pygame.image.load('data/asteroid.png'))

# pygame.display.toggle_fullscreen()

running = True
clock = pygame.time.Clock()

# music
pygame.mixer.music.load('data/music/song18.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

# objects
objGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
tirosGroup = pygame.sprite.Group()

# Objetos
fundo = pygame.sprite.Sprite(objGroup)
fundo.image = pygame.image.load('data/fundo.png')
fundo.image = pygame.transform.scale(fundo.image, display.get_size())
fundo.rect = fundo.image.get_rect()

player = Player(objGroup)
asteroids = []
contador = 0
limite = 120


# game loop
def render():
    display.fill([0, 0, 0])
    objGroup.draw(display)
    pygame.display.update()


def update():
    objGroup.update()

    # Novos asteroids
    global contador
    global limite
    contador += 1
    if contador > limite:
        asteroids.append(Asteroid(objGroup, asteroidGroup))
        contador = 0
        limite = randint(100, 120)

    # Colisões
    colisoes = pygame.sprite.spritecollide(player, asteroidGroup, False)
    if colisoes:
        global running
        running = False

    # Tiro

while running:
    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tiro = Plasma(objGroup, tirosGroup)
                tiro.rect.center = player.rect.center
                print('sla')
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
