import pygame
from body import Body


class Player(Body):
    # variables
    speed: int

    # functional methods
    def write(self, subscription: str, pos: list):
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        text = font.render(subscription, True, [200, 200, 200], None)
        textRect = text.get_rect()
        textRect.x = pos[0]
        textRect.y = pos[1]
        self.display.blit(text, textRect)

    # initializing method
    def __init__(self, display):
        super().__init__(1)
        self.display = display
        self.speed = 1

        # self.addVelocity(10, 90)
        # self.addAcceleration(1, 90)
        # self.addForce(1, 90)

        self.x = 200

    def update(self, delta_time: float, buttons: list):
        # inputs
        if buttons[0]:
            self.addVelocity(self.speed, 180)
        if buttons[1]:
            self.addVelocity(self.speed, -90)
        if buttons[2]:
            self.addVelocity(self.speed, 0)
        if buttons[3]:
            self.addVelocity(self.speed, 90)
        # super method
        super().update(delta_time)

    def render(self):
        rect = pygame.rect.Rect(self.x, self.y, 100, 100)
        pygame.draw.rect(self.display, [200, 200, 200], rect)

        self.write('position:     [{:.2f}, {:.2f}]'.format(self.x, self.y), [2, 2])
        self.write('DeltaSpace:   {}'.format(self.getDeltaSpace()), [2, 20])
        self.write('velocity:     [{:.2f}, {:.2f}]'.format(self.velocityX, self.velocityY), [2, 40])
        self.write('acceleration: [{:.2f}, {:.2f}]'.format(self.accelerationX, self.accelerationY), [2, 60])