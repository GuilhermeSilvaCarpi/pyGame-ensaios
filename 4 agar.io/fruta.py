from pygame import Rect
from bolha import Bolha
from random import randint
from math import dist

class Fruta(Bolha):
    bolhas: list

    def __init__(self, janela: Rect, bolhas: list):
        # iniciando parâmetros
        super().__init__(janela, bolhas)
        self.angulo = [0, 0]
        self.cor = [200, 200, 0]
        self.raio = 1.5
        self.bolhas = bolhas
        self.janela = janela

        # definindo posição
        arranjandolugar = True
        while arranjandolugar:
            self.x = randint(0, janela.w)
            self.y = randint(0, janela.h)
            for bolha in bolhas:
                if dist([self.x, self.y], [bolha.x, bolha.y]) < bolha.raio:
                    break
            else:
                arranjandolugar = False

    def update(self):
        pass

    def altodestruição(self):
        self.__init__(self.janela, self.bolhas)
