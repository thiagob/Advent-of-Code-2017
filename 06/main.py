data = open("06\input.txt").readline()
data = map(lambda c: int(c), data.split('\t'))

class MemoryBanks:

    def __init__(self, data):
        self.data = data
        self.count = 0
        self.combinations = []

    def balance(self):
        if self.data in self.combinations:
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
    print m.data

print m.count