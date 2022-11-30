# import pygame
from math import radians, sin, cos


class Body:
    x: int
    y: int
    accelerationX: float
    accelerationY: float

    # functional methods
    def deltaSpace(self, deltatime: float):
        # velocity ups with acceleration
        self.velocityX += self.accelerationX / 100
        self.velocityY += self.accelerationY / 100

        # position change with velocity
        self.x += int(self.velocityX * deltatime) / 1000
        self.y += int(self.velocityY * deltatime) / 1000

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

    def update(self, deltatime: float):
        self.deltaSpace(deltatime)

    def render(self):
        pass
