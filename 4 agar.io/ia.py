from bolha import Bolha
from pygame import Rect
from math import dist

class Ia(Bolha):
    def update(self, bolhas: list, frutas: list):
        alvo = [0, 0]
        menorDistancia = self.janela.w + self.janela.h
        for bolha in bolhas:
            if bolha != self:
                # qual tem a menor distancia
                if dist([self.x, self.y], [bolha.x, bolha.y]) < menorDistancia:
                    menorDistancia = dist([self.x, self.y], [bolha.x, bolha.y])
                    alvo = [bolha.x, bolha.y]
                    if bolha.raio > self.raio:
                        alvo = [-bolha.x, -bolha.y]
        else:
            self.apontaPara(alvo)
        self.bolhas = bolhas
        super().update(bolhas, frutas)
