import pygame
from body import Body


class Player(Body):
    # initializing method
    def __init__(self, display):
        self.display = display

        self.speed = 3

        super().__init__(1)

        self.addForce(0.08, 0)

    def update(self, buttons):
        if buttons[0]:
            self.y -= self.speed
        if buttons[1]:
            self.x -= self.speed
        if buttons[2]:
            self.y += self.speed
        if buttons[3]:
            self.x += self.speed
        super().update()

    def render(self):
        rect = pygame.rect.Rect(self.x, self.y, 100, 100)
        pygame.draw.rect(self.display, [200, 200, 200], rect)

        font = pygame.font.Font(None, 32)
        text = font.render('GeeksForGeeks', True, [200, 200, 200], None)
        textRect = text.get_rect()
