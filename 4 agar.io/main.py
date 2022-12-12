import pygame
from bolha import Bolha
from jogador import Jogador
from fruta import Fruta
from ia import Ia

# Iniciando pygame
pygame.init()
pygame.display.set_caption('Agar.io')
display = pygame.display.set_mode([600, 600])
rectDisplay = display.get_rect()
isRunning = True
clock = pygame.time.Clock

# Objetos
blobs = [Jogador(rectDisplay, [300, 300])]
for i in range(20):
    blobs.append(Ia(rectDisplay, blobs))

frutas = []
for i in range(140):
    frutas.append(Fruta(rectDisplay, blobs))

# loop
def update():
    for obj in blobs:
        obj.update(rectDisplay, blobs, frutas)
    for fruta in frutas:
        fruta.update()

def render():
    display.fill([50, 50, 50])

    for fruta in frutas:
        fruta.render(display)
    for obj in blobs:
        obj.render(display)

    pygame.display.update()


while isRunning:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
            break
    clock().tick(60)
    update()
    render()
