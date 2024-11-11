import pygame

from config import NUM_OF_ANTS, ANTHILL_POINT_1, ANTHILL_POINT_2, GREEN, BLUE
from classes.Ant import Ant
from config import screen

class Nest:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.ants = [Ant(self.x, self.y) for _ in range(NUM_OF_ANTS)]
        self.food_level = 100
        self.colour = colour

    def draw_nest(self):
        pygame.draw.circle(screen, self.colour, self.location, radius=20)

    def move_ants(self):
        for ant in self.ants:
            ant.move(self.location)

    def draw_ants(self):
        for ant in self.ants:
            ant.draw(screen, self.colour)

Nest1 = Nest(ANTHILL_POINT_1[0], ANTHILL_POINT_1[1], GREEN)
Nest2 = Nest(ANTHILL_POINT_2[0], ANTHILL_POINT_2[1], BLUE)