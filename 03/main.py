import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Spiral:

    def __init__(self, size):
        self.size = size
        self.init_matrix()

    def init_matrix(self):
        self.current = 0
        self.matrix = np.zeros(shape=(self.size, self.size))
        self.x, self.y = self.starting_point()

    def starting_point(self):
        center = len(self.matrix) / 2
        return center, center
    
    def fill(self, input):
        self.init_matrix()

        movement = Direction.DOWN
        while self.current < input:
            movement = self.next_direction(movement)
            self.current += 1
            self.assign(self.current)
            self.move(movement)

    def stress_test(self, input):
        self.init_matrix()
        
        adjs = 0
        movement = Direction.DOWN

        while True:
            movement = self.next_direction(movement)
            adjs = self.adjacents()
            self.assign(adjs)

            if adjs > input:
                break;            

            self.move(movement)
        return adjs

    def next_direction(self, movement):
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
        return movement

    def move(self, direction):
        if direction == Direction.RIGHT:
            self.y += 1
        elif direction == Direction.LEFT:
            self.y -= 1
        elif direction == Direction.UP:
            self.x -= 1
        elif direction == Direction.DOWN:
            self.x += 1

        if self.x+1 >= len(self.matrix) or self.y+1 >= len(self.matrix):
            raise Exception('Not enough space!')

    def assign(self, value):
        self.matrix[self.x, self.y] = value
            

    def adjacents(self):
        adjs = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                adjs.append(self.matrix[self.x + x, self.y + y])
        return sum(adjs) if sum(adjs) > 0 else 1

    def manhattan_distance(self, data):
        start = self.starting_point()
        position = self.find(data)
        distance = [abs(start[0] - position[0]), abs(start[1] - position[1])]
        return sum(distance)

    def find(self, data):
        size = len(self.matrix)

        for x in range(0, size):
            for y in range(0, size):
                if self.matrix[x,y] == data:
                    return [x, y]
        
        raise Exception('Item was not found!')





input = 265149

if True:
    s = Spiral(600)
    s.fill(input)
    print s.manhattan_distance(input)

if True:
    s = Spiral(600)
    print s.stress_test(265149)