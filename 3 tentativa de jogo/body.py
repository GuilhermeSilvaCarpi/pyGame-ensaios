# import pygame
from math import radians, sin, cos
from time import time


class Body:
    x: int
    y: int
    accelerationX: float
    accelerationY: float

    # functional methods
    def deltaSpace(self):

        it = self.ft
        self.ft = time()
        dt = self.ft - it

        # velocity ups with acceleration
        self.velocityX += self.accelerationX
        self.velocityY += self.accelerationY

        # position change with velocity
        self.x += int(self.velocityX)
        self.y += int(self.velocityY)

    def addVelocity(self, intensity: float, angle: float):
        # v = position change
        self.velocityX += intensity * sin(radians(angle))
        self.velocityY += intensity * cos(radians(angle))

    def addAcceleration(self, intensity: float, angle: float):
        # a = velocity variation
        self.accelerationX += intensity * sin(radians(angle))
        self.accelerationY += intensity * cos(radians(angle))

    def addForce(self, intensity: float, angle: float):
        # f = m * a
        # a = f / m
        intensity /= self.mass
        self.accelerationX += intensity * sin(radians(angle))
        self.accelerationY += intensity * cos(radians(angle))

    # mains methods
    def __init__(self, mass: float):
        self.ft = 0
        self.mass = mass
        self.x, self.y = 0, 0
        self.velocityX, self.velocityY = 0, 0
        self.accelerationX, self.accelerationY = 0, 0

    def update(self):
        self.deltaSpace()

    def render(self):
        pass
