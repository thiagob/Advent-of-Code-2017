data = list(open('12\input.txt').readlines())
data = map(lambda l: l.strip().replace(' ', '').split('<->'), data)
data = map(lambda a: [a[0], a[1].split(',')], data)


class Program():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.childs = {}

    def add_child(self, child):
        self.childs[child.name] = child
        child.parent = self

class ProgramList():
    def __init__(self):
        self.programs = {}
        self.clear_links()

    def get_program(self, name):
        if not name in self.programs:
            self.add(Program(name))
        return self.programs[name]

    def add(self, program):
        self.programs[program.name] = program

    def process(self, input):
        for line in input:
            program = self.get_program(line[0])

            for connection in line[1]:
                program.add_child(self.get_program(connection))


    def clear_links(self):
        self.links = []

    def get_links(self, program):
        self.links.append(program.name)
        for sub in program.childs:
            if not sub in self.links:
                self.get_links(mngr.get_program(sub))
        return set(self.links)

    def get_groups(self):
        count = 0
        remaining = self.programs.keys()
        while len(remaining) > 0:
            program = remaining[0]
            
            self.clear_links()
            links = self.get_links(mngr.get_program(program))
            
            for link in links:
                remaining.remove(link)
            count += 1
        return count


mngr = ProgramList()
mngr.process(data)

mngr.clear_links()
print len(mngr.get_links(mngr.get_program('0')))

print mngr.get_groups()