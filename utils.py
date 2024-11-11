import random
from config import FOOD_SPAWN_RANGE

def sq_dist(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2

def spawn_food(food_manager, x, y, amount):
    for _ in range(amount):
        food_x = random.uniform(x - FOOD_SPAWN_RANGE, x + FOOD_SPAWN_RANGE)
        food_y = random.uniform(y - FOOD_SPAWN_RANGE, y + FOOD_SPAWN_RANGE)
        food_manager.add(int(food_x), int(food_y))
