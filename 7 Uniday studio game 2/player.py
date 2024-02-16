import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    v = 2
    aceleracao = 0.1

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/player.png')
        self.image = pygame.transform.scale(self.image, [16 * 4, 16 * 4])
        self.rect = pygame.Rect(50, 50, self.image.get_width(), self.image.get_height())

        pygame.mixer.init()
        self.sons = [pygame.mixer.Sound('data/sounds/laser1.mp3'),
                     pygame.mixer.Sound('data/sounds/laser5.mp3'),
                     pygame.mixer.Sound('data/sounds/laser9.mp3')]

    def update(self, *args):
        # teclas pressionadas
        keys_presseds = pygame.key.get_pressed()
        if keys_presseds[pygame.K_UP]:
            self.v -= self.aceleracao
        elif keys_presseds[pygame.K_DOWN]:
            self.v += self.aceleracao
        else:
            self.v *= 0.9
        if keys_presseds[pygame.K_SPACE]:
            self.sons[randint(0, 2)].play()

        # movimennto
        self.rect.y += self.v

        # limites tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.v = 0
        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.v = 0
