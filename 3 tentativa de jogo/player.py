import pygame
from body import Body


class Player(Body):
    # variables
    speed: int
    rect: pygame.Rect

    # functional methods
    def write(self, subscription: str, pos: list):
        font = pygame.font.Font('regular.otf', 15)
        text = font.render(subscription, True, [200, 200, 200], None)
        textRect = text.get_rect()
        textRect.x = pos[0]
        textRect.y = pos[1]
        self.display.blit(text, textRect)

    # initializing method
    def __init__(self, display):
        super().__init__(1, display)
        self.display = display
        self.speed = 1

        # self.addVelocity(10, 90)
        # self.addAcceleration(1, 90)
        # self.addForce(1, 90)

        self.pos[0] = 400
        self.pos[1] = 200
        # self.addAcceleration(10, 360)
        self.addVelocityTo(10, [0, 0])
        self.rect = pygame.Rect(0, 0, 100, 100)

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
        #
        self.rect.center = [self.pos[0], self.pos[1]]

        # super method
        super().update(delta_time)

    def render(self):
        pygame.draw.rect(self.display, [200, 200, 200], self.rect)

        self.write('position:     [{:.2f}, {:.2f}]'.format(self.pos[0], self.pos[1]), [2, 2])
        self.write('DeltaSpace:   [{:.2f}, {:.2f}]'.format(self.getDeltaSpace()[0], self.getDeltaSpace()[1]), [2, 20])
        self.write('velocity:     [{:.2f}, {:.2f}]'.format(self.velocity[0], self.velocity[1]), [2, 40])
        self.write('acceleration: [{:.2f}, {:.2f}]'.format(self.acceleration[0], self.acceleration[1]), [2, 60])

        super().render()
