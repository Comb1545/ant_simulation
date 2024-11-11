import pygame

# Screen size
WIDTH, HEIGHT = 900, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Simulation parameters
ANTHILL_POINT_1 = (20, HEIGHT // 2)
ANTHILL_POINT_2 = (WIDTH - 20, HEIGHT // 2)
PHEROMONE_STRENGTH = 100
ANT_SPEED = 1
NUM_OF_ANTS = 300
PHEROMONE_DETECTION_RANGE_SQUARED = 200 ** 2
FOOD_DETECTION_RANGE_SQUARED = 100 ** 2
FOOD_COLLECTION_RANGE_SQUARED = 10 ** 2
DIRECTION_TOLERANCE = .7

RANDOM_ANT_DIRECTION = 0 # +- value to randomly move
# 0.2 is good for simulations but 0 is fun to watch with no food

DIRECTION_CHANGE_COOLDOWN = 5
MAX_FOOD_AMOUNT = 1
PHEROMONE_COOLDOWN = 30
FOOD_SPAWN_RANGE = 40
FOOD_SPAWN_AMOUNT_PER_CLICK = 40
SPATIAL_PARTITIONING_COLS = 32
SPATIAL_PARTITIONING_ROWS = 18