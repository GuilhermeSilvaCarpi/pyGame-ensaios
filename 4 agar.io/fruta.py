from pygame import Rect
from bolha import Bolha


class Fruta(Bolha):
    rect = None
    bolhas: list

    def __init__(self, rect: Rect, bolhas: list):
        super().__init__(rect, bolhas)
        self.angulo = [0, 0]
        self.cor = [200, 200, 0]
        self.raio = 2
        self.rect = rect
        self.bolhas = bolhas

    def update(self):
        pass

    def render(self, display):
        super().render(display)

    def altodestruição(self):
        self.__init__(self.rect, self.bolhas)