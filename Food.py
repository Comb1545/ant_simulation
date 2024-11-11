import pygame
from config import RED

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), 1)