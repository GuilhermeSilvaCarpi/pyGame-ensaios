import pygame
from math import radians, sin, cos

class Corpo():
    x: int
    y: int
    mass: float
    velocityX: float
    velocityY: float
    accelerationX: float
    accelerationY: float

    # metodos funcionais


    def deltaSpace(self):
        # velocidade aumenta de acordo com aceleração
        self.velocityX += self.acelerationX
        self.velocityY += self.acelerationY
        # posição varia de acordo dcom a velocidade
        self.x += int(self.velocidadeX)
        self.y += int(self.velocidadeY)

    def addVelocity(self, intensity: float, angle: float):
        #v = variação de posição
        self.velocityX += intensity * sin(radians(angle))
        self.velocityY += intensity * cos(radians(angle))

    def addAcceleration(self, intensity: float, angle: float):
        # a = varição de velocidade
        self.accelerationX += intensity * sin(radians(angle))
        self.accelerationY += intensity * cos(radians(angle))

    def addForce(self, intensity: float, angle: float):
        # f = m * a
        # a = f / m
        intensity /= self.mass
        self.accelerationX += intensity * sin(radians(angle))
        self.accelerationY += intensity * cos(radians(angle))

    # metodos principais
    def __init__(self, mass: float):
        self.mass = mass
    def update(self):
        self.deltaSpace()
    def render(self):
        pass