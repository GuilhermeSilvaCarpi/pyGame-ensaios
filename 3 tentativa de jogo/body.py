from pygame import draw
from math import radians, sin, cos, dist


class Body:
    pos: [float, float]
    velocity: [float, float]
    acceleration: [float, float]
    deltaX: float
    deltaY: float

    # functional methods
    def deltaSpace(self, delta_time: float):
        # velocity increases with acceleration
        self.velocity[0] += self.acceleration[0] * delta_time
        self.velocity[1] += self.acceleration[1] * delta_time
        # getting initial position to calculate variance
        iX = self.pos[0]
        iY = self.pos[1]
        # space variation. position increases with velocity
        self.pos[0] += self.velocity[0] * delta_time
        self.pos[1] += self.velocity[1] * delta_time
        # delta space calculation
        fX = self.pos[0]
        fY = self.pos[1]
        self.deltaX = (fX - iX) / delta_time
        self.deltaY = (fY - iY) / delta_time

    def addVelocity(self, intensity: float, angle: float):
        # velocity is position variation
        self.velocity[0] += intensity * sin(radians(angle))
        self.velocity[1] += intensity * cos(radians(angle))

    def addVelocityTo(self, intensity: float, direction: [int, int]):
        # get distances
        rd = dist(self.pos, direction)  # real distance
        xd = self.pos[0] - direction[0]  # x distance
        yd = self.pos[1] - direction[1]  # y distance

        # calculating sin and cos
        sinD = yd / rd
        cosD = xd / rd

        # changing vector speeds
        self.velocity[0] -= cosD * intensity
        self.velocity[1] -= sinD * intensity

    def addAcceleration(self, intensity: float, angle: float):
        # acceleration is velocity variation
        self.acceleration[0] += intensity * sin(radians(angle))
        self.acceleration[1] += intensity * cos(radians(angle))

    def addForce(self, intensity: float, angle: float):
        # f = m * a
        # a = f / m
        intensity /= self.mass
        self.acceleration[0] += intensity * sin(radians(angle))
        self.acceleration[1] += intensity * cos(radians(angle))

    # mains methods
    def __init__(self, mass: float, display):
        self.ft = 0
        self.mass = mass
        self.pos = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.display = display

    def update(self, delta_time: float):
        self.deltaSpace(delta_time)

    def render(self):
        # draw vectors
        draw.line(self.display, [200, 0, 200],
                  self.pos, [self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1]], 3)
        draw.line(self.display, [200, 0, 0],
                  self.pos, [self.pos[0] + self.velocity[0], self.pos[1]], 3)
        draw.line(self.display, [0, 0, 200],
                  self.pos, [self.pos[0], self.pos[1] + self.velocity[1]], 3)

        # draw shape

    def getDeltaSpace(self):
        # returns the space variation in a frame
        return [self.deltaX, self.deltaY]
