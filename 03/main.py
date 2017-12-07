import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Spiral:

    def __init__(self):
        self.current = 0
        self.matrix = np.zeros(shape=(1000, 1000))
        self.x, self.y = starting_point(self.matrix)
    
    def assign(self):
        self.current += 1
        self.matrix[self.x, self.y] = self.current

    def move(self, direction):
        if direction == Direction.RIGHT:
            self.y += 1
        elif direction == Direction.LEFT:
            self.y -= 1
        elif direction == Direction.UP:
            self.x -= 1
        elif direction == Direction.DOWN:
            self.x += 1

        if self.x >= len(self.matrix) or self.y >= len(self.matrix):
            raise Exception('Not enough space!')


    def fill(self, max):
        movement = Direction.DOWN

        while self.current < max:
            if movement == Direction.RIGHT:
                # upper cel is empty and upper right cel was not filled yet
                if (self.matrix[self.x + 1, self.y] == 0 and self.matrix[self.x - 1, self.y] == 0):
                    movement = Direction.UP
            elif movement == Direction.UP:
                # left cel is empty, move left
                if (self.matrix[self.x, self.y - 1] == 0):
                    movement = Direction.LEFT
            elif movement == Direction.LEFT:
                # lower cel is empty, move down
                if (self.matrix[self.x + 1, self.y] == 0):
                    movement = Direction.DOWN
            elif movement == Direction.DOWN:
                # right cel is empty, move right
                if (self.matrix[self.x, self.y + 1] == 0):
                    movement = Direction.RIGHT
                
            self.assign()
            self.move(movement)

def starting_point(matrix):
    center = len(matrix) / 2
    return center, center

def find(matrix, data):
    size = len(matrix) - 1

    for x in range(0, size):
        for y in range(0, size):
            if matrix[x,y] == data:
                return [x, y]
    
    raise Exception('Item was not found!')

def manhattan_distance(matrix, data):
    start = starting_point(matrix)
    position = find(matrix, data)

    distance = [abs(start[0] - position[0]), abs(start[1] - position[1])]
    return sum(distance)

input = 265149

s = Spiral()
s.fill(input)
print manhattan_distance(s.matrix, input)