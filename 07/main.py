import re

data = list(open('07\input.txt').readlines())
data = map(lambda l: l.split('->'), data)

print data

class Tower():

    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.parent = None
        self.childs = {}

    def add_child(self, child):
        self.childs[child.name] = child
        child.parent = self

class TowersList():
    def __init__(self):
        self.towers = {}

    def get_tower(self, name):
        if not name in self.towers:
            self.add(Tower(name))
        return self.towers[name]
            
    def add(self, tower):
        self.towers[tower.name] = tower

    def process(self, input):
        for item in input:
            parts = item[0].split(' ')

            name = parts[0]
            weight = int(re.findall(r'\d+', parts[1])[0])

            tower = self.get_tower(name)
            tower.weight = weight

            if len(item) == 2:
                names = item[1].strip().split(', ')
                for name in names:
                    tower.add_child(self.get_tower(name))

    def get_main_tower(self):
        for key in self.towers:
            tower = self.towers[key]
            if not tower.parent:
                return tower

lst = TowersList()
lst.process(data)
print lst.get_main_tower().name