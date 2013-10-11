__author__ = 'bcm'
import math
from common import Colors as C

import pygame

class Edge():
    def __init__(self, source, target, weight=15):
        self.source = source
        self.target = target
        self.weight = weight
        self.color = C.edge_color


    def is_directed(self):
        return False

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
                         int(self.weight)+3)
        pygame.draw.line(screen, self.color,
                        (self.source.x, self.source.y),
                        (self.target.x, self.target.y),
                         int(self.weight))

class DirectedEdge():

    is_directed = True

    def __init__(self, source, target, weight=4):
        self.source = source
        self.target = target
        self.weight = weight #int
        self.color = C.edge_color

    def __str__(self):
        return "(" + str(self.source) + " -> " + str(self.target) + ")"

    def __eq__(self, other):
        return self.source is other.source and \
               self.target is other.target

    def display(self, screen):
        pygame.draw.line(screen, self.color,
                        (self.source.x, self.source.y),
                        (self.target.x, self.target.y),
                         int(self.weight))
        sourcex, sourcey = int(self.source.x), int(self.source.y)
        targetx, targety = int(self.target.x), int(self.target.y)
        dy = sourcey - targety
        dx = sourcex - targetx
        rotate_by = math.fabs(math.degrees(math.atan2(-dy, dx) % (2 * math.pi)))
        arrow = pygame.Surface((300, 300))
        pygame.draw.polygon(arrow, self.color, ((0, 150), (300, 300), (300, 0)))
        d = pygame.transform.rotozoom(arrow, rotate_by, .02 * self.weight)
        d.set_colorkey(C.color_black)

        posx = int((sourcex + targetx * 3.5) / 4.5) - d.get_width() / 2
        posy = int((sourcey + targety * 3.5) / 4.5) - d.get_height() / 2
        screen.blit(d, (posx, posy))
        #
        #for x in range(100):
        #    w = x / 2
        #    den = 1 + w
        #    posx = int((sourcex + targetx * w) / den) - d.get_width() / 2
        #    posy = int((sourcey + targety * w) / den) - d.get_height() / 2
        #    screen.blit(d, (posx, posy))
        #
        #
        #
        #
