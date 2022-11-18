import pygame


class Bixin(pygame.sprite.Sprite):
    ve = 5

    def __init__(self, *groups):

        super().__init__(*groups)
        self.image = pygame.image.load('data/bixin_b.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 170, 100, 100)

    def update(self):

        if self.rect.x >= 400:
            self.ve = -2
        elif self.rect.x <= 50:
            self.ve = 2
        self.rect.x += self.ve
