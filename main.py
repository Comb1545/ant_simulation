import pygame
import math

from config import *
from classes.Manager import food_manager, pheromone_manager
from classes.Ant import ants
from utils import spawn_food


def draw_grid():
    for row in range(SPATIAL_PARTITIONING_ROWS):
        tile_height = HEIGHT // SPATIAL_PARTITIONING_ROWS
        tile_width = WIDTH // SPATIAL_PARTITIONING_COLS
        for col in range(SPATIAL_PARTITIONING_COLS):
            pygame.draw.rect(screen, GRAY, (col * tile_width, row * tile_height, tile_width, tile_height), width=1)

def draw_radius():
    for ant in ants:
        pygame.draw.circle(screen, WHITE, (ant.x, ant.y), radius=math.sqrt(FOOD_DETECTION_RANGE_SQUARED), width=1)

def draw_tile(coords):
    tile_height = HEIGHT // SPATIAL_PARTITIONING_ROWS
    tile_width = WIDTH // SPATIAL_PARTITIONING_COLS
    pygame.draw.rect(screen, GREEN, (coords[1] * tile_width, coords[0] * tile_height, tile_width, tile_height), width=3)


# Pygame initialization
pygame.init()
clock = pygame.time.Clock()

# Spawning initial food
#spawn_food(food_manager, 480, 150, FOOD_SPAWN_AMOUNT_PER_CLICK * 3)
#spawn_food(food_manager, 480, 930, FOOD_SPAWN_AMOUNT_PER_CLICK * 3)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            spawn_food(food_manager, x, y, FOOD_SPAWN_AMOUNT_PER_CLICK)
    screen.fill(BLACK)
    # Draw pheromones
    for row in pheromone_manager.repository:
        for tile in row:
            for pheromone in tile:
                pheromone.decay()
                if pheromone.strength == 0:
                    pheromone_manager.remove(pheromone)
                    break
                else:
                    pheromone.draw(screen)
  
    pygame.draw.circle(screen, YELLOW, ANTHILL_POINT, radius=20)

    # Move and draw ants
    for ant in ants:
        ant.move()
        ant.draw(screen, GREEN)

    # Draw food
    for row in food_manager.repository:
        for tile in row:
            for food in tile:
                food.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
