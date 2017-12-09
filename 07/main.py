import re

data = list(open('07\input.txt').readlines())
data = map(lambda l: l.split('->'), data)

class Tower():

    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.parent = None
        self.childs = {}

    def add_child(self, child):
        self.childs[child.name] = child
        child.parent = self

    def get_weight(self):
        if len(self.childs) == 0:
            return self.weight
        else:
            total_weight = 0
            for child in self.childs:
                total_weight += self.childs[child].get_weight()
            return total_weight  + self.weight

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

def find_unbalaced_tower(tower, level):
    for t in tower.childs:
        child = tower.childs[t]
        print " " * 2 * level + child.name + " " + str(child.get_weight()) + " " + str(child.weight)
        
        for s in child.childs:
            continue
            find_unbalaced_tower(child.childs[s], level + 1)

lst = TowersList()
lst.process(data)
main = lst.get_main_tower()

print main.name + " " + str(main.get_weight()) + " " + str(main.weight)

find_unbalaced_tower(lst.get_tower('hlqnsbe'), 1)
print '----------'
find_unbalaced_tower(lst.get_tower('rilyl'), 2)
print '----------'
find_unbalaced_tower(lst.get_tower('aurik'), 3)
print '----------'
find_unbalaced_tower(lst.get_tower('jriph'), 4)

# done via debug
lst.get_tower('jriph').weight = 1993