data = list(open('19\input.txt').readlines())

class Routing():

    def load(self, grid):
        self.grid = grid
        self.x = -1
        self.y = -1
        self.direction = None
        self.path = []
        self.steps = 0

    def goto_start(self):
        for idx, val in enumerate(self.grid[0]):
            if val != ' ':
                self.x = idx
                self.y = 0
                self.set_direction('down')
                return True

        raise Exception('Not able to find starting point')

    def walk(self):
        pos = self.get_position()
        if pos.isalpha():
            self.append(pos)
            self.go(self.direction)
        elif pos in ['|', '-']:
            self.go(self.direction)
        elif pos == '+':
            if self.direction in ['right', 'left']:
                if self.get_position(0, -1) == '|' or self.get_position(0, -1).isalpha():
                    self.go('up')
                elif self.get_position(0, 1) == '|' or self.get_position(0, 1).isalpha():
                    self.go('down')
                else:
                    raise Exception('Not able to move 1')
            else:
                if self.get_position(-1, 0) == '-' or self.get_position(-1, 0).isalpha():
                    self.go('left')
                elif self.get_position(1, 0) == '-' or self.get_position(1, 0).isalpha():
                    self.go('right')
                else:
                    raise Exception('Not able to move 2')
        else:
            print 'Movement stopped!'
            print 'Path is {0}'.format(''.join(self.path))
            print 'Total of movments: {0}'.format(self.steps)
            self.direction = None

    def get_position(self, delta_x=0, delta_y=0):
        x = self.x + delta_x
        y = self.y + delta_y
        if x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid):
            return self.grid[y][x]
        else:
            return False

    def go(self, direction):
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'left':
            self.x -= 1
        self.set_direction(direction)
        self.steps += 1

    def set_direction(self, direction):
        self.direction = direction
        print 'Going to {0}. Next pos is {1}'.format(direction, self.get_position())

    def append(self, pos):
        self.path.append(pos)
        print self.path


r = Routing()
r.load(data)
r.goto_start()
while r.direction != None:
    r.walk()