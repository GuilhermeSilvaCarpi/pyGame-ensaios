import pygame
from player import Player
from cenario import Cenario

# iniciando
pygame.init()
running = True
clock = pygame.time.Clock()
display = pygame.display.set_mode([600, 600])
pygame.display.set_caption('jogo')
# grupos
grupo = pygame.sprite.Group()
# objetos

# fundo = pygame.sprite.Sprite(grupo)
# fundo.image = pygame.image.load('data/cenarios/casa.png')
# fundo.image = pygame.image.load('data/cenarios/estudio.png')
# fundo.image = pygame.image.load('data/cenarios/rua.png')
"""fundo.image = pygame.image.load('data/cenarios/corredor.jpg')
fundo.image = pygame.transform.scale(fundo.image, [fundo.image.get_width() / 2,
                                                   fundo.image.get_height() / 2])
fundo.rect = fundo.image.get_rect()"""

player = Player(grupo, display)
# # cenarios
"""cenarios = [Cenario(grupo, 'data/cenarios/casa.png', [10, 10], 1),
            Cenario(grupo, 'data/cenarios/corredor.jpg', [186, 260], 125),
            Cenario(grupo, 'data/cenarios/estudio.png', [10, 10], 1),
            Cenario(grupo, 'data/cenarios/rua.png', [10, 10], 1)]"""


# frame
def update():
    player.update()


def render():
    display.fill([200, 200, 200])

    grupo.draw(display)
    player.render()

    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    update()
    render()
