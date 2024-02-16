import pygame


class Plasma(pygame.sprite.Sprite):
    v = 4

    def __init__(self, *groups):
        self.image = pygame.image.load('data/plasma.png')
        self.image = pygame.transform.scale(self.image, [8 * 4, 8 * 4])
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

    def update(self):
        self.rect.x += self.v
        if self.rect.left > 800:
            self.kill()
