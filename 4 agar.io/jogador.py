import pygame
from bolha import Bolha

class Jogador(Bolha):
    # main
    def __init__(self, rect: pygame.Rect, pos: [float, float]):
        bolhas = [self]
        super().__init__(rect, bolhas)
        self.x = pos[0]
        self.y = pos[1]

        self.mousePos = None
        self.cor = [100, 100, 200]

    # loop
    def update(self,  rect: pygame.Rect, bolhas: list, frutas: list):
        self.mousePos = pygame.mouse.get_pos()
        self.apontaPara(self.mousePos)
        super().update(rect, bolhas, frutas)


    def render(self, display):
        super().render(display)
        pygame.draw.circle(display, [100, 100, 100], self.mousePos, 10, 3)
