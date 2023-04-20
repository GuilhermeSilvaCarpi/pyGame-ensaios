import pygame
from entity import Entity


class Player(Entity):
    # Variables
    speed: float

    # Methods
    def __init__(self):
        self.velocity = 10
        self.commands = {'item 1': False,
                         'item 2': False,
                         'up': False,
                         'down': False,
                         'left': False,
                         'right': False}
        super().__init__(20, 20, 100, 100)

    def frameUpdate(self):
        if self.commands['up']:
            self.moveIn(self.velocity, 0)
        if self.commands['left']:
            self.moveIn(self.velocity, 270)
        if self.commands['down']:
            self.moveIn(self.velocity, 180)
        if self.commands['right']:
            self.moveIn(self.velocity, 90)

    def render(self, display: pygame.Surface):
        pygame.draw.rect(display, [100, 100, 100], self)
