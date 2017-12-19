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

    def execute(self, commands):
        for cmd in commands:
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

        return ''.join(self.programs)

def part1_sample():
    data = ['s1', 'x3/4', 'pe/b']
    d = Dance(get_programs('e'))
    print d.execute(data)

def part1_input():
    d = Dance(get_programs('p'))
    print d.execute(data)

# part1_sample()
part1_input()