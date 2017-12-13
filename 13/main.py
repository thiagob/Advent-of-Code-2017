data = list(open('13\input.txt').readlines())
data = map(lambda l: l.strip().split(': '), data)
data = map(lambda a: [int(a[0]), int(a[1])], data)

print data

class Firewall():

    def __init__(self):
        self.position = 0
        self.layers = {}
        self.severity = 0
        self.layers_count = 0

    def load(self, data):
        for d in data:
            self.layers[d[0]] = {
                "range" : d[1],
                "scan" : 1,
                "step": 1
            }

        self.layers_count = data[-1][0]

    def clock(self):
        self.position += 1
        for l in self.layers:
            layer = self.layers[l]
            layer["scan"] += layer["step"]
            if layer["scan"] == layer["range"] and layer["step"] == 1:
                layer["step"] = -1
            elif layer["scan"] == 1 and layer["step"] == -1:
                layer["step"] = 1

    def calc_severity(self):
        if self.is_caught():
            self.severity += self.layers[self.position]["range"] * self.position

    def is_caught(self):
        if self.position in self.layers:
            return self.layers[self.position]["scan"] == 1
        else:
            return False

    def transmit(self):
        while self.position < self.layers_count:
            self.clock()
            self.calc_severity()
        return self.severity


fwl = Firewall()
fwl.load(data)
print fwl.transmit()