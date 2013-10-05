__author__ = 'bcm'
from common import Colors as C

import pygame

class Edge():
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = 30
        self.color = C.edge_color

    def __str__(self):
        return "(" + str(self.source) + ", " + str(self.target) + ")"

    def __eq__(self, other):
        for me in (self.target, self.source):
            if not me in (other.source, other.target):
                return False
        return True

    def display(self, screen):
        pygame.draw.line(screen, C.background_color,
                        (self.source.x, self.source.y),
                        (self.target.x, self.target.y),
                         int(self.weight/2)+3)
        pygame.draw.line(screen, self.color,
                        (self.source.x, self.source.y),
                        (self.target.x, self.target.y),
                         int(self.weight/2))