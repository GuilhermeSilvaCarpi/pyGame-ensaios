from pygame import Rect
from bolha import Bolha


class Fruta(Bolha):
    bolhas: list

    def __init__(self, janela: Rect, bolhas: list):
        super().__init__(janela, bolhas)
        self.angulo = [0, 0]
        self.cor = [200, 200, 0]
        self.raio = 2
        self.bolhas = bolhas

    def update(self):
        pass

    def render(self, display):
        super().render(display)

    def altodestruição(self):
        self.__init__(self.janela, self.bolhas)