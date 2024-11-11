import pygame
from config import PHEROMONE_STRENGTH

class Pheromone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.strength = PHEROMONE_STRENGTH  # Pheromone strength (fades over time)

    def decay(self):
        if self.strength > 0:
            self.strength -= 1
    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, int(self.strength / PHEROMONE_STRENGTH * 255)), (self.x, self.y), 3)
