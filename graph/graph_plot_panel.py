__author__ = 'bcm'
import pygame
from random import sample, choice
from Vertex import Vertex
from Edge import Edge
from common import Colors as C

__author__ = 'bcm'

from pygame.locals import *
import pygame
import random
import math

class GraphPlotPanel():

    def __init__(self, width=1280, height=700, dampen=.01,
                 dampen_decrease=.001, pad_scaler=3, view_size_scaler=1,
                 mouse_sens=.4, number_of_vertices=1, number_of_edges=0, edge_rate=.01,
                 force_max=30, debug=False):
        """
        dampen: how 'smushy' the animations happen (use between .01 and .001)

        dampen_decrease:    the rate at which the dampening increases after
                            adding an edge or a node, (0 means none)

        pad_scaler changes the force output of nodes, in (2.5,  4) are good

        view_size_scaler increases the visual size of nodes and edges
        debug:  shows lines denoting the force vectors on vertices!

        we can fill in the number of nodes and edges to begin with.
        (This is for randomized graph view)
            number_of_vertices
            number_of_edges
            edge_rate

        mouse_sens controls panning speed

        force_max limits max force (use if there's lots of vibrations)

        """
        self.width = width
        self.height = height
        self.selected_bg = False
        self.selected_vertex = None
        self.hovered_vertex = None
        self.running = True
        self.frame_count = 0
        self.dampen = dampen
        self.dampen_decrease = 1 - dampen_decrease
        self.E = []
        self.V = []
        self.view_size_scaler = view_size_scaler
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = number_of_edges
        self.edge_rate = edge_rate
        self.mouse_sens = mouse_sens
        self.debug = debug
        self.force_max = force_max
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.info_font = pygame.font.SysFont("monospace", 20)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Graph Visualizer')

    def shake(self):
        for v in self.V:
            move_by = choice([1, -1])
            v.dx = move_by * len(self.V) * 500
            move_by = choice([1, -1])
            v.dy = move_by * len(self.V) * 500

    def findvertex(self, x, y):
        for v in self.V:
            if math.hypot(v.x - x, v.y - y) <= v.size * self.view_size_scaler:
                return v
        return None

    def spring(self, edge):
        self._spring(edge.source, edge.target, edge.weight, edge=True)

    def _spring(self, v1, v2, weight, edge):
        pad = 4 * ((v1.size + v2.size) + int(.5 * len(self.V)))
        x_diff = v1.x - v2.x
        y_diff = v1.y - v2.y
        angle = math.atan2(y_diff, x_diff)
        dist = math.hypot(x_diff, y_diff)
        force = 10 * (dist - pad)
        if force > self.force_max:
            force = self.force_max
        if edge:
            force = 20 * (dist - pad / 2)
        x_force = math.cos(angle) * force
        y_force = math.sin(angle) * force
        v1.dx += x_force
        v2.dx -= x_force
        v1.dy += y_force
        v2.dy -= y_force

    def repel(self, v1):
        for v2 in self.V:
            if v2 == v1:
                return
            self._spring(v1, v2, 300, edge=False)

    def pan(self, x, y):
        for v in self.V:
            v.x += x * self.mouse_sens
            v.y += y * self.mouse_sens

    # def buildRandomGraph(self, number_of_vertices, edge_rate):
    #     for n in range(self.):
    #         size = choice([k for k in range(5, 25, 5)])
    #         v = Vertex(size)
    #         self.V.append(v)

    def add_vertex(self):
        #reset dampening
        self.dampen = self.dampen
        v = Vertex()
        v.x = choice(range(self.width))
        v.y = choice(range(self.height))
        self.V.append(v)

    def add_edge(self):
        num_vertex = len(self.V)
        num_edges = len(self.E)
        max_edges = num_vertex * (num_vertex -1) / 2
        if num_vertex > 1 and num_edges < max_edges:
            edges = sample(self.V, 2)
            e = Edge(edges[1], edges[0], 20)
            while e in self.E:
                edges = sample(self.V, 2)
                e = Edge(edges[1], edges[0], 20)
            e.source.degree += 1
            e.target.degree += 1
            self.E.append(e)

    def clear_graph(self):
        self.E = []
        self.V = []

    def calculate_positions(self):
        for e in self.E:
            self.spring(e)
        for v in self.V:
            if self.debug:
                pygame.draw.line(self.screen, C.monokai_green,
                                (v.x, v.y), (v.x + v.dx * 3, v.y + v.dy * 3), 3)
            # if self.dampen > 1e-05:
            self.repel(v)
            if math.fabs(v.dx) > 1000:
                v.dx *= .7
            if math.fabs(v.dy) > 1000:
                v.dy *= .7
            v.dx = v.dx * self.dampen
            v.dy = v.dy * self.dampen
            v.move()

    def key_event_handler(self):
        for event in pygame.event.get():
                #checking pressed keys
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_s]:
                        self.shake()
                    if keys[pygame.K_v]:
                        if event.mod & KMOD_SHIFT:
                            for x in range(10):
                                self.add_vertex()
                        else:
                            self.add_vertex()
                        # self.add_vertex()
                    if keys[pygame.K_e]:
                        if event.mod & KMOD_SHIFT:
                            for x in range(10):
                                self.add_edge()
                        else:
                            self.add_edge()
                    if keys[pygame.K_z]:
                        self.clear_graph()
                        # self.edges = []
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    self.selected_vertex = self.findvertex(mouseX, mouseY)
                    if self.selected_vertex:
                        self.selected_vertex.border_color = C.selected_color
                    else:
                        self.selected_bg = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_vertex:
                        self.selected_vertex.border_color = C.vertex_boarder_color
                    self.selected_vertex = None
                    self.selected_bg = False
                elif event.type == pygame.MOUSEMOTION:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    found = self.findvertex(mouseX, mouseY)
                    if found:
                        self.hovered_vertex = found
                        self.hovered_vertex.border_color = C.selected_color
                        self.hovered_vertex.color = C.selected_color
                    elif self.hovered_vertex:
                        self.hovered_vertex.border_color = C.vertex_boarder_color
                        self.hovered_vertex.color = C.vertex_color
                        self.hovered_vertex = None

    def run(self):
        while(self.running):
            self.frame_count += 1
            self.dampen *= self.dampen_decrease
            self.key_event_handler()
            self.screen.fill(C.background_color)
            if self.selected_vertex:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                self.selected_vertex.x = mouseX
                self.selected_vertex.y = mouseY
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LCTRL]:
                    self.pan(int(mouseX - self.width / 2) * -.2,
                            (int(mouseY - self.height / 2) * -.2))
            if self.selected_bg:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                # if math.fabs(mouseX) + math.fabs(mouseY) < 500:
                self.pan(int(mouseX - self.width / 2) * -.2,
                        (int(mouseY - self.height / 2) * -.2))
            self.calculate_positions()

            for e in self.E:
                if e.source == self.selected_vertex or\
                   e.target == self.selected_vertex or\
                   e.source == self.hovered_vertex or\
                   e.target == self.hovered_vertex:
                    e.color = C.selected_color
                else:
                    e.color = C.edge_color
                e.display(self.screen)
            for v in self.V:
                v.display(self.screen)
            vertex_number_info = self.info_font.render(
                "Vertices: " + str(len(self.V)),
                1,
                C.debug_color)
            edge_number_info = self.info_font.render(
                "    Edges: " + str(len(self.E)),
                1,
                C.debug_color)
            fps_number_info = self.info_font.render(
                "      FPS: " + str(self.fpsClock.get_fps())[:5],
                1,
                C.debug_color)
            self.screen.blit(vertex_number_info, (10, 10))
            self.screen.blit(edge_number_info, (10, 30))
            self.screen.blit(fps_number_info, (10, 50))
            pygame.display.flip()
            self.fpsClock.tick(120)