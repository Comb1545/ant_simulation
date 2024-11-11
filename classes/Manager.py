from collections import deque
from config import *
from classes.Food import Food
from classes.Pheromones import Pheromone

class Manager():
    def __init__(self, obj_class):
        self.repository = [[set() for _ in range(SPATIAL_PARTITIONING_COLS)] for _ in range(SPATIAL_PARTITIONING_ROWS)] # list of sets
        self.obj_class = obj_class
        self.tile_width = WIDTH // SPATIAL_PARTITIONING_COLS
        self.tile_height = HEIGHT // SPATIAL_PARTITIONING_ROWS

    def checkOverlap(self, sq_R, Xc, Yc, row, col):
        # https://www.geeksforgeeks.org/check-if-any-point-overlaps-the-given-circle-and-rectangle/
        X1 = col * (WIDTH // SPATIAL_PARTITIONING_COLS)
        Y1 = row * (HEIGHT // SPATIAL_PARTITIONING_ROWS)
        X2 = (col+1) * (WIDTH // SPATIAL_PARTITIONING_COLS)
        Y2 = (row+1) * (HEIGHT // SPATIAL_PARTITIONING_ROWS)
        # check if circle is inside the tile

        # Find the nearest point on the
        # rectangle to the center of
        # the circle
        Xn = max(X1, min(Xc, X2))
        Yn = max(Y1, min(Yc, Y2))

        # Find the distance between the
        # nearest point and the center
        # of the circle
        # Distance between 2 points,
        # (x1, y1) & (x2, y2) in
        # 2D Euclidean space is
        # ((x1-x2)**2 + (y1-y2)**2)**0.5
        Dx = Xn - Xc
        Dy = Yn - Yc

        return (Dx ** 2 + Dy ** 2) <= sq_R
        # returns true if tile overlaps with ant radius, false otherwise
    def check(self, x, y, sq_radius):
        row = y // self.tile_height
        col = x // self.tile_width
        if row >= SPATIAL_PARTITIONING_ROWS:
            row = SPATIAL_PARTITIONING_ROWS - 1
        if col >= SPATIAL_PARTITIONING_COLS:
            col = SPATIAL_PARTITIONING_COLS - 1

        q = deque()
        q.append((int(row), int(col)))
        checked = set()
        checked.add((row, col))
        modifications = ((-1, 0), (0, -1), (1, 0), (0, 1))
        output = []
        while q:
            (row, col) = q.popleft()
            if self.checkOverlap(sq_radius, x, y, row, col):
                output.append((self.repository[row][col], (row, col)))
                checked.add((row, col))

                for mod in modifications:
                    new_tile = (int(row + mod[0]), int(col + mod[1]))
                    # The last condition in the line below isn't really valid, but it improves performance and ants still fulfill their goal, so I decided to leave it.
                    # Just making sure you're aware of that if you decide to play with the code.
                    if new_tile not in checked and new_tile not in q and new_tile[0] >= 0 and new_tile[0] < SPATIAL_PARTITIONING_ROWS and new_tile[1] >= 0 and new_tile[1] <  SPATIAL_PARTITIONING_COLS and self.repository[new_tile[0]][new_tile[1]]:
                        q.append(new_tile)
        return output
        # returns list of sets
    def add(self, x, y):
        row = y // self.tile_height
        col = x // self.tile_width
        if row < SPATIAL_PARTITIONING_ROWS and col < SPATIAL_PARTITIONING_COLS:
            self.repository[row][col].add(self.obj_class(x, y))
    def remove(self, obj):
        row = obj.y // self.tile_height
        col = obj.x // self.tile_width
        if obj in self.repository[row][col]:
            self.repository[row][col].remove(obj)
            return True
        return False

# init objects
food_manager = Manager(Food)
pheromone_manager = Manager(Pheromone)