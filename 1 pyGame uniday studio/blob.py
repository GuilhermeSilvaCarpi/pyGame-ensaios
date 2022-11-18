import pygame

v = 1


class Blob(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/bixin.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, *args):
        # teclas pressionadas
        keys_presseds = pygame.key.get_pressed()
        if keys_presseds[pygame.K_w]:
            self.rect.y -= v
        if keys_presseds[pygame.K_s]:
            self.rect.y += v
        if keys_presseds[pygame.K_a]:
            self.rect.x -= v
        if keys_presseds[pygame.K_d]:
            self.rect.x += v

        #limites tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 400:
            self.rect.bottom = 400
        if self.rect.right > 800:
            self.rect.right = 800
