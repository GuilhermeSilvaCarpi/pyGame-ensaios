import pygame
from math import sin, cos, radians, dist


class Entity(pygame.Rect):
    # other methods
    def moveIn(self, velocity: float, angle: float):
        self.x += sin(radians(angle)) * velocity
        self.y -= cos(radians(angle)) * velocity

    def moveTo(self, destination: [float, float], velocity):
        # variables
        dX = self.x - destination[0]
        dY = self.y - destination[1]
        d = dist([self.x, self.y], destination)
        angSin = dX/d
        angCos = dY/d

        # angle
        '''ang = 0
        self.moveIn(velocity, ang)'''
        self.x -= angSin * velocity
        self.y -= angCos * velocity

    # initializing
    def __init__(self, x: float, y: float, w: float, h: float):
        super().__init__(x, y, w, h)

    # loop
    def frameUpdate(self):
        pass

    def render(self, display: pygame.Surface):
        pygame.draw.rect(display, [255, 255, 255, 50], self, 3)
