# import pygame
from math import radians, sin, cos

import pygame.draw


class Body:
    x: float
    y: float
    deltaX: float
    deltaY: float
    accelerationX: float
    accelerationY: float

    # functional methods
    def deltaSpace(self, delta_time: float):
        # velocity increases with acceleration
        self.velocityX += self.accelerationX * delta_time
        self.velocityY += self.accelerationY * delta_time
        # getting initial position to calculate variance
        iX = self.x
        iY = self.y
        # space variation. position increases with velocity
        self.x += self.velocityX * delta_time
        self.y += self.velocityY * delta_time
        # delta space calculation
        fX = self.x
        fY = self.y
        self.deltaX = (fX - iX) / delta_time
        self.deltaY = (fY - iY) / delta_time

    def addVelocity(self, intensity: float, angle: float):
        # velocity is position variation
        self.velocityX += intensity * sin(radians(angle))
        self.velocityY += intensity * cos(radians(angle))

    def addAcceleration(self, intensity: float, angle: float):
        # acceleration is velocity variation
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

    def update(self, delta_time: float):
        self.deltaSpace(delta_time)

    def render(self):
        pass

    def getDeltaSpace(self):
        # returns the space variation in a frame
        return [self.deltaX, self.deltaY]
