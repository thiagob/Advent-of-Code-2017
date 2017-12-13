data = list(open('13\input.txt').readlines())
data = map(lambda l: l.strip().split(': '), data)
data = map(lambda a: [int(a[0]), int(a[1])], data)


class Firewall():

    def __init__(self):
        self.layers = {}
        self.layers_count = 0
        self.packages = []

    def load(self, data):
        self.packages = []
        for d in data:
            self.layers[d[0]] = {
                "range" : d[1],
                "scan" : 1,
                "step": 1
            }

        self.layers_count = data[-1][0]

    def register(self, package):
        self.packages.append(package)
    
    def unregister(self, package):
        self.packages.remove(package)

    def clock(self):
        for pkg in self.packages:
            pkg.clock()

        for l in self.layers:
            layer = self.layers[l]
            layer["scan"] += layer["step"]
            if layer["scan"] == layer["range"] and layer["step"] == 1:
                layer["step"] = -1
            elif layer["scan"] == 1 and layer["step"] == -1:
                layer["step"] = 1
    
class Package():
    
    def __init__(self, firewall, delay=0):
        self.delay = delay
        self.position = -1 if delay == 0 else (-1 * delay) - 1
        self.severity = 0

        self.caughted = False
        self.transmitted = False

        self.firewall = firewall
        self.firewall.register(self)

    def calculate_severity(self):
        self.severity += self.firewall.layers[self.position]["range"] * self.position

    def is_caught(self):
        if self.position in self.firewall.layers:
            return self.firewall.layers[self.position]["scan"] == 1
        else:
            return False

    def clock(self):
        self.position += 1
        if self.is_caught():
            self.caughted = True
            self.calculate_severity()
        if self.position > self.firewall.layers_count:
            self.transmitted = True

    def to_s(self):
        return { 
            "delay": self.delay, 
            "severity": self.severity,
            "position": self.position,
            "caughted": self.caughted,
            "transmitted": self.transmitted }

def first_part(delay=0, skip=False):
    fwl = Firewall()
    fwl.load(data)

    package = Package(fwl, delay)
    while (not package.transmitted):
        fwl.clock()
        if package.caughted:
            break

    return package

def forca_bruta():
    delay = 0
    while True:
        pkg = first_part(delay)
        if not pkg.caughted and pkg.transmitted:
            return pkg
        delay += 1

def second_part():
    fwl = Firewall()
    fwl.load(data)

    delay = 0
    while True:
        p = Package(fwl, delay)
        p.position = -1

        fwl.clock()

        i = 0
        while (i < len(fwl.packages) - 1) :
            pkg = fwl.packages[i]
            
            if pkg.caughted:
                fwl.packages.remove(pkg)
            else:
                i += 1

            if pkg.transmitted:
                return pkg

        if delay % 50000 == 0:
            print delay
        delay += 1

# pkg = first_part()
# print pkg.to_s()

# pkg = first_part(10)
# print pkg.to_s()

# pkg = forca_bruta()
# print pkg.to_s()

pkg = second_part()
print pkg.to_s()