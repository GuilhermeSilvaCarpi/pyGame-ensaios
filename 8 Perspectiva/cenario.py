import pygame


class Cenario:
    fundo: pygame.sprite.Sprite
    pontoDeFuga: [int, int]
    alturaCamera: int

    def __init__(self, grupo: pygame.sprite.Group, arquivo: str, pontoDeFuga: [int, int], alturaCamera: int):
        self.fundo = pygame.sprite.Sprite(grupo)
        self.fundo.image = pygame.image.load(arquivo)
        self.fundo.rect = self.fundo.image.get_rect()
        self.pontoDeFuga = pontoDeFuga
        self.alturaCamera = alturaCamera
