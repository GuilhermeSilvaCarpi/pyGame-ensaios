import pygame
from math import radians, sin, cos, dist
from random import randint

class Bolha:
    # variáveis
    x: float
    y: float
    raio: float
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

    def absorção(self, bolhas: list, rect: pygame.Rect):
        for bolha in bolhas:
            # se está comivel
            if dist([self.x, self.y], [bolha.x, bolha.y]) < self.raio:
                # se for maior
                if bolha.raio < self.raio:
                    self.raio += bolha.raio * 0.2
                    bolha.altodestruição(bolhas, rect)

    def altodestruição(self, bolhas: list, rect: pygame.Rect):
        bolhas.remove(self)
        del self
        # self.__init__(rect, bolhas)

    def comerFruta(self, frutas: list):
        frutose = 2

        for fruta in frutas:
            if dist([self.x, self.y], [fruta.x, fruta.y]) < self.raio:
                self.raio += frutose
                fruta.altodestruição()

    # main
    def __init__(self, rect: pygame.Rect, bolhas: list):
        # posicap
        self.x = randint(0, rect.w)
        self.y = randint(0, rect.h)

        # iniciando atributos
        self.raio = 5
        self.velocidade = 2
        self.mudarAngulo(0)
        self.cor = [100, 200, 100]

        self.raio += randint(0, 3)

    # loop
    def update(self,  rect: pygame.Rect, bolhas: list, frutas: list):
        self.absorção(bolhas, rect)
        self.movimento()
        self.comerFruta(frutas)
        # limitação conforme arena
        if self.x - self.raio < 0:
            self.x = self.raio
        elif self.x + self.raio > rect.w:
            self.x = rect.w - self.raio
        if self.y - self.raio < 0:
            self.y = self.raio
        elif self.y + self.raio > rect.h:
            self.y = rect.h - self.raio

    def render(self, display):
        pygame.draw.circle(display, self.cor, [self.x, self.y], self.raio)
