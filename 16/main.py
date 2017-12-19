import datetime

data = list(open('16\input.txt').readlines())
data = data[0].strip().split(',')

def get_programs(last):
    programs = []
    for i in range(ord('a'), ord(last) + 1):
        programs.append(chr(i))
    return programs


class Dance():

    def __init__(self, programs):
        self.programs = programs
        self.count = 0

    def spin(self, x):
        self.programs = self.programs[-x:] + self.programs[:-x]

    def exchange(self, a, b):
        prg_a = self.programs[a]
        prg_b = self.programs[b]

        self.programs[a] = prg_b
        self.programs[b] = prg_a

    def partner(self, a, b):
        prg_a = self.programs.index(a)
        prg_b = self.programs.index(b)

        self.exchange(prg_a, prg_b)

    def execute(self, commands, limit=0):
        while True:
            for cmd in commands:
                self.count += 1

                if cmd[0] == 's':
                    param = int(cmd[1:])
                    self.spin(param)
                elif cmd[0] == 'x':
                    params = [int(p) for p in cmd[1:].split('/')]
                    self.exchange(params[0], params[1])
                elif cmd[0] == 'p':
                    params = cmd[1:].split('/')
                    self.partner(params[0], params[1])
                else:
                    raise Exception('Not able to parse: "{0}"'.format(cmd))

                if limit > 0:
                    if self.count >= limit:
                        return

                    # notify every 10%
                    progress = float(self.count) / limit * 100
                    if progress % 1 == 0:
                        print '{0}% ({1}/{2})'.format(progress, self.count, limit)
                        self.print_result()
                        print ''

            if limit == 0:
                return

    def print_result(self):
        print { "programs": ''.join(self.programs), "count": self.count, "now": str(datetime.datetime.now().time()) }

def part1_sample():
    data = ['s1', 'x3/4', 'pe/b']
    d = Dance(get_programs('e'))
    d.execute(data)
    d.print_result()

def part1_input(dance):
    d.execute(data)
    d.print_result()

def part2_input(dance):
    d.execute(data, 1000000000) 
    d.print_result()

# part1_sample()

d = Dance(get_programs('p'))
part1_input(d)
part2_input(d)