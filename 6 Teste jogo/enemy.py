import pygame
from entity import Entity
from player import Player


class Enemy(Entity):
    def __init__(self):
        super().__init__(500, 250, 100, 100)
        self.velocity = 2

    def frameUpdate(self, player: Player):
        self.moveTo([player.x, player.y], self.velocity)

    def render(self, display: pygame.Surface):
        super().render(display)
