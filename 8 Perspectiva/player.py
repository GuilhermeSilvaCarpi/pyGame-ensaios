import pygame


class Player:
    x: int
    y: int
    v: int
    pontoDeFuga: [int, int]
    imagem: pygame.sprite.Sprite

    def __init__(self, grupo: pygame.sprite.Group, display):
        # fundo
        self.fundo = pygame.sprite.Sprite(grupo)

        """self.pontoDeFuga, self.alturaCamera, self.fundo.image = [186, 260], 200, pygame.image.load(
            'data/cenarios/corredor.jpg')
        self.fundo.image = pygame.transform.scale(self.fundo.image, [self.fundo.image.get_width() / 2,
                                                                     self.fundo.image.get_height() / 2])"""
        self.pontoDeFuga, self.alturaCamera, self.fundo.image = [-65, 350], 220, pygame.image.load('data/cenarios/casa.png')
        # # self.pontoDeFuga, self.alturaCamera, self.fundo.image = [230, 200], 180, pygame.image.load('data/cenarios/estudio.png')
        # # self.pontoDeFuga, self.alturaCamera, self.fundo.image = [245, 248], 220, pygame.image.load('data/cenarios/rua.png')
        """self.pontoDeFuga, self.alturaCamera, self.fundo.image = [297, 195], 214, pygame.image.load('data/cenarios/Desenho perspectiva.jpg')
        self.fundo.image = pygame.transform.scale(self.fundo.image, [self.fundo.image.get_width() * 0.12,
                                                                     self.fundo.image.get_height() * 0.12])"""

        self.fundo.rect = self.fundo.image.get_rect()

        # personagem
        self.referencia = pygame.image.load('data/personagem.png')
        self.referencia = pygame.transform.scale(self.referencia,
                                                 [self.referencia.get_width() / 2,
                                                  self.referencia.get_height() / 2])

        self.imagem = pygame.sprite.Sprite(grupo)
        self.imagem.image = pygame.image.load('data/personagem.png')
        self.imagem.image = pygame.transform.scale(self.imagem.image,
                                                   [self.imagem.image.get_width() / 2,
                                                    self.imagem.image.get_height() / 2])
        self.imagem.rect = self.imagem.image.get_rect()

        # outras variaveis
        self.display = display
        self.x, self.y = 0, 0
        self.v = 2

    def update(self):
        # inputs
        pressionados = pygame.key.get_pressed()
        # # mvcimento
        if pressionados[pygame.K_LEFT]:
            self.x -= self.v
        if pressionados[pygame.K_UP]:
            self.y -= self.v
        if pressionados[pygame.K_RIGHT]:
            self.x += self.v
        if pressionados[pygame.K_DOWN]:
            self.y += self.v
        # # camera
        if pressionados[pygame.K_w]:
            self.alturaCamera += 10
        if pressionados[pygame.K_s]:
            self.alturaCamera -= 10

        # imagem

        self.imagem.image = pygame.transform.scale(self.referencia,
                                                   [self.referencia.get_width() * self.y / self.alturaCamera,
                                                    self.referencia.get_height() * self.y / self.alturaCamera])
        self.imagem.rect.x = self.pontoDeFuga[0] + self.x * self.y / 125
        self.imagem.rect.y = self.pontoDeFuga[1] + self.y - self.imagem.image.get_height()

    def render(self):
        pygame.draw.circle(self.display, [150, 200, 150], self.pontoDeFuga, 10, 2)
        pygame.draw.line(self.display, [150, 150, 200], [0, self.pontoDeFuga[1]], [600, self.pontoDeFuga[1]], 2)
        pygame.draw.circle(self.display, [200, 200, 200], self.pontoDeFuga, 2)
