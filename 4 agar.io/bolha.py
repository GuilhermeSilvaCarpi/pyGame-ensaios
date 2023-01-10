import pygame
from math import radians, sin, cos, dist
from random import randint

class Bolha:
    # variáveis
    x: float
    y: float
    raio: float
    janela: pygame.Rect
    velocidade = float
    angulo = [float, float]
    cor = [int, int, int]

    # métodos funcionais
    def mudarAngulo(self, graus):
        self.angulo = [sin(radians(graus)), cos(radians(graus))]

    def apontaPara(self, pos: [float, float]):
        dX = self.x - pos[0]
        dY = self.y - pos[1]
        d = dist(pos, [self.x, self.y])

        try:
            self.angulo[0] = -(dX / d)
            self.angulo[1] = -(dY / d)
        except:
            self.angulo = [0, 0]

    def movimento(self):
        novaVelocidade = self.velocidade / self.raio * 10
        self.x += self.angulo[0] * novaVelocidade
        self.y += self.angulo[1] * novaVelocidade
        # self.x += sin(radians(self.angulo)) * self.velocidade
        # self.y += cos(radians(self.angulo)) * self.velocidade

    def absorção(self, bolhas: list):
        for bolha in bolhas:
            # se está comivel
            if dist([self.x, self.y], [bolha.x, bolha.y]) < self.raio:
                # se for maior
                if bolha.raio < self.raio:
                    self.raio += bolha.raio * 0.2
                    bolha.altodestruição(bolhas)

    def altodestruição(self, bolhas: list):
        bolhas.remove(self)
        del self
        # self.__init__(rect, self.janela)

    def comerFruta(self, frutas: list):
        frutose = 1.5

        for fruta in frutas:
            if dist([self.x, self.y], [fruta.x, fruta.y]) < self.raio:
                self.raio += frutose
                fruta.altodestruição()

    # main
    def __init__(self, janela: pygame.Rect, bolhas: list):
        # posição
        self.x = randint(0, janela.w)
        self.y = randint(0, janela.h)

        # iniciando atributos
        self.raio = 5
        self.velocidade = 2
        self.mudarAngulo(0)
        self.cor = [100, 200, 100]
        self.janela = janela

        self.raio += randint(0, 3)

    # loop
    def update(self, bolhas: list, frutas: list):
        self.absorção(bolhas)
        self.movimento()
        self.comerFruta(frutas)
        # limitação tamanho
        if self.raio > self.janela.w / 2:
            self.raio = self.janela.w / 2
        if self.raio > self.janela.h / 2:
            self.raio = self.janela / 2
        # limitação conforme arena
        if self.x - self.raio < 0:
            self.x = self.raio
        elif self.x + self.raio > self.janela.w:
            self.x = self.janela.w - self.raio
        if self.y - self.raio < 0:
            self.y = self.raio
        elif self.y + self.raio > self.janela.h:
            self.y = self.janela.h - self.raio

    def render(self, display):
        pygame.draw.circle(display, self.cor, [self.x, self.y], self.raio)
