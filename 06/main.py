data = open("06\input.txt").readline()
data = map(lambda c: int(c), data.split('\t'))

class MemoryBanks:

    def __init__(self, data):
        self.data = data
        self.count = 0
        self.combinations = []
        self.loops_count = 0

    def balance(self):
        if self.data in self.combinations:
            index = self.combinations.index(self.data)
            self.loops_count = len(self.combinations) - index
            return False
        else:
            self.combinations.append(self.data[:])
            
            tank = self.get_bigger_tank_index()
            self.distribute_tank_blocks(tank)
            
            self.count += 1
            return True

    def get_bigger_tank_index(self):
        return self.data.index(max(self.data))
    
    def distribute_tank_blocks(self, tank):
        blocks = self.data[tank]
        self.data[tank] = 0

        index = tank
        for b in range(0, blocks):
            index = index + 1 if index < len(self.data) - 1 else 0
            self.data[index] += 1

##############################################

m = MemoryBanks(data)

while m.balance():
    pass

print m.count
print m.loops_count