import pygame
from random import randint


class Asteroid(pygame.sprite.Sprite):
    v: int

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('data/asteroid.png')
        self.image = pygame.transform.scale(self.image, [16 * 4, 16 * 4])
        self.image = pygame.transform.rotate(self.image, 90 * randint(0,  3))

        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = randint(0, 400 - self.rect.h)
        self.v = randint(1, 4)

    def update(self):
        self.rect.x -= self.v
        if self.rect.right < 0:
            self.kill()
