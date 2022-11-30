import pygame
from body import Body


class Player(Body):

    # metodos funcionais
    def write(self, subscription: str, pos: list):
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(subscription, True, [200, 200, 200], None)
        textRect = text.get_rect()
        textRect.x = pos[0]
        textRect.y = pos[1]
        self.display.blit(text, textRect)
    # initializing method
    def __init__(self, display):
        super().__init__(1)
        self.display = display
        self.speed = 3

        self.addVelocity(1, 0)
        self.addAcceleration(1, 0)
        #self.addForce(1, 0)

        self.x = 150

    def update(self, buttons: list, deltatime: float):
        # inputs
        if buttons[0]:
            self.y -= self.speed
        if buttons[1]:
            self.x -= self.speed
        if buttons[2]:
            self.y += self.speed
        if buttons[3]:
            self.x += self.speed
        #
        self.write(str(deltatime), [2, 100])
        # metodo super
        super().update(deltatime)

    def render(self):
        rect = pygame.rect.Rect(self.x, self.y, 100, 100)
        pygame.draw.rect(self.display, [200, 200, 200], rect)

        self.write('posição [{}, {}]'.format(self.x, self.y), [2, 2])
        self.write('velocityX: {}'.format(self.velocityX), [2, 20])
        self.write('velocityY: {}'.format(self.velocityY), [2, 40])
        self.write('accelerationX: {}'.format(self.accelerationX), [2, 60])
        self.write('accelerationY: {}'.format(self.accelerationX), [2, 80])
