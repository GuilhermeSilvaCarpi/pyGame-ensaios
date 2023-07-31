import pygame
from math import dist


class Triangle:
    # Variables
    points: list
    lines: list
    area: float
    pos: [float, float]

    # Other methods
    def getVariables(self):
        print('\033[035m-' * 50)
        print('''{cian}Position: {yellow}{}
        {cian}Points: {yellow}{}
        {cian}Lines: {yellow}{}
        {cian}Area: {yellow}{}\033[m'''.format(self.pos, self.points, self.lines, self.area,
                                               yellow='\033[033m', cian='\033[36m'))

    def pointInside(self, point: [float, float]):
        subTri = []
        for index in range(len(self.points)):
            subTri.append(Triangle([
                point,
                self.points[index],
                self.points[index - 1]]))

        subAreas = subTri[0].area + subTri[1].area + subTri[2].area
        marginOfError = 1
        if subAreas <= self.area + marginOfError:
            return True
        else:
            return False

    # Initializing
    def __init__(self, points: list):
        # Points
        self.points = points[0: 3]

        # Cor
        self.color = [200, 200, 200]

        # MediumPoint
        mediumPoint = [0, 0]
        for point in self.points:
            mediumPoint[0] += point[0]
            mediumPoint[1] += point[1]
        else:
            mediumPoint[0] /= len(self.points)
            mediumPoint[1] /= len(self.points)
        self.pos = mediumPoint

        # Relative points
        self.relativePoints = []
        for index in range(len(self.points)):
            self.relativePoints.append([self.points[index][0] - self.pos[0],
                                        self.points[index][1] - self.pos[1]])

        # Lines
        self.lines = []
        for index in range(len(self.points)):
            self.lines.append(dist(self.points[index - 1], self.points[index]))
        else:
            self.lines.append(self.lines[0])
            self.lines.pop(0)

        # Perimeter
        perimeter = 0
        for line in self.lines:
            perimeter += line

        # Area. Using Heron´s formula
        # S = √(p*(p-a)*(p-b)*(p-c))
        self.area = 1.0
        p = perimeter / 2  # Semi perimeter

        for line in self.lines:
            self.area *= (p - line)
        self.area = (p * self.area) ** 0.5

        # if area is a "complex" data, convert to float
        if type(self.area) == complex:
            self.area = self.area.real

    # Loop
    def update(self):
        for index in range(len(self.points)):
            self.points[index][0] = self.pos[0] + self.relativePoints[index][0]
            self.points[index][1] = self.pos[1] + self.relativePoints[index][1]

    def render(self, display: pygame.Surface):
        """for point in self.points:  # Distance from medium point to each point
            pygame.draw.circle(display, [60, 60, 60], self.pos, dist(self.pos, point), 2)"""

        pygame.draw.polygon(display, self.color, self.points, 2)  # Triangle
        pygame.draw.circle(display, [220, 220, 220], self.pos, 2)  # Medium point

        for point in self.points:
            pygame.draw.circle(display, [200, 200, 200], point, 10, 2)
