puzzle = list(open('22\input.txt').readlines())
puzzle = map(lambda l: l.strip(), puzzle)

directions = ["left", "up", "right", "down"]

class Cluster():

    def __init__(self):
        self.initial_state = {}
        self.infected_nodes = {}
        self.infections = 0
        self.current_position = (0,0)
        self.direction = None

    def load(self, puzzle):
        height = len(puzzle)
        width = len(puzzle[0])

        for row in range(0, height):
            for col in range(0, width):
                if puzzle[row][col] == '#':
                    x = col - int(height / 2)
                    y = row - int(width / 2)
                    self.infect((x,y))

        self.infections = 0
        self.initial_state = self.infected_nodes.copy()

    def infect(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        self.infected_nodes[coordinate] = 'I'
        if not self.started_infected():
            self.infections += 1

    def started_infected(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        return self.initial_state.has_key(coordinate)

    def is_infected(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        return self.infected_nodes.has_key(coordinate) and self.infected_nodes[coordinate] == 'I'

    def weaken(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        self.infected_nodes[coordinate] = 'W'

    def is_weakened(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        return self.infected_nodes.has_key(coordinate) and self.infected_nodes[coordinate] == 'W'

    def flag(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        self.infected_nodes[coordinate] = 'F'

    def is_flagged(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        return self.infected_nodes.has_key(coordinate) and self.infected_nodes[coordinate] == 'F'

    def clean(self, coordinate=None):
        coordinate = self.current_position if coordinate is None else coordinate
        return self.infected_nodes.pop(coordinate, None)

    def burst(self, times=None):
        times = 1 if times is None else times

        for _ in range(0, times):
            if self.is_infected():
                self.turn_right()
                self.flag()
            elif self.is_flagged():
                self.reverse_direction()
                self.clean()
            elif self.is_weakened():
                self.infect()
            else: # clean
                self.turn_left()
                self.weaken()
            self.move()

    def move(self):
        x = 0
        y = 0

        if self.direction == "left":
            x = -1
        elif self.direction == "right":
            x = 1
        elif self.direction == "down":
            y = 1
        elif self.direction == "up":
            y = -1
            
        self.current_position = (self.current_position[0] + x, self.current_position[1] + y)
        

    def turn_left(self):
        if self.direction == None:
            self.direction = "left"
        else:
            self.turn(-1)

    def turn_right(self):
        if self.direction == None:
            self.direction = "right"
        else:
            self.turn(1)

    def reverse_direction(self):
        self.turn(2)

    def turn(self, k):
        self.direction = directions[(directions.index(self.direction) + k) % len(directions)]
        return self.direction


c = Cluster()
c.load(puzzle)
print len(c.infected_nodes)

c.burst(10000000)
print c.infections