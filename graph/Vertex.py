__author__ = 'bcm'
import pygame
from random import random, choice
from common import Colors as C

class Vertex():
    def __init__(self, inner_color=C.vertex_color,
                       outer_color=C.vertex_boarder_color,
                       view_size_scaler=1,
                       name=None):
        self.name = name
        self.x = None
        self.y = None
        self.dx = int(random() * 100)
        self.dy = int(random() * 100)
        self.thickness = 0
        self.color = inner_color
        self.border_color = outer_color
        self.degree = 0
        self.size = 30
        self.view_size_scaler = view_size_scaler
        if self.name is None:
            self.name = 30

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.name == other.name

    def display(self, screen):
        #fill
        pygame.draw.circle(screen, self.border_color, (
            int(self.x), int(self.y)), self.size * self.view_size_scaler + 3)
        #outline
        pygame.draw.circle(screen, self.color, (
            int(self.x), int(self.y)), self.size * self.view_size_scaler,
                                                 self.thickness)




        fontObj = pygame.font.Font(None, max(self.size, 12))
        label = fontObj.render(str(self.name), False, C.word_color)

        #pygame.draw.ellipse(screen, self.color, (int(self.x), int(self.y)),
        #                   (self.x - label.get_width() / 2,
        #                    self.y - label.get_height() / 2))

        screen.blit(label, (int(self.x - label.get_width() / 2),
                            int(self.y - label.get_height() / 2)))

    def move(self):
        self.x -= self.dx
        self.y -= self.dy