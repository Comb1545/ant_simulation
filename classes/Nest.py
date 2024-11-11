import pygame

from config import NUM_OF_ANTS
from classes.Ant import Ant
from config import screen

class Nest:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.ants = [Ant(x, y) for _ in range(NUM_OF_ANTS)]
        self.food_level = 100
        self.colour = colour

    def draw_nest(self):
        pygame.draw(screen, self.colour, (self.x, self.y), radius=20)

    def add_ant(self, ant):
        self.ants.append(ant)

    def remove_ant(self, ant):
        if ant in self.ants:
            self.ants.remove(ant)

    def move_ants(self):
        for ant in self.ants:
            ant.move()

    def draw_ants(self):
        for ant in self.ants:
            ant.draw(screen, self.colour)