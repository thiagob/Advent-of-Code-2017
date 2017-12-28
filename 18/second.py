import sys
import threading
import time

instructions = list(open('18\input.txt').readlines())
instructions = map(lambda i: i.strip().split(' '), instructions)

class Program(threading.Thread):

    def __init__(self, id, instructions):
        threading.Thread.__init__(self)

        self.variables = {}
        self.played_sound = 0
        self.id = id
        self.variables['p'] = id
        self.queue = []
        self.linked_program = None
        self.waiting = False
        self.instructions = instructions
        self.abort = False
        self.sending_count = 0
        self.offset = 0

    def run(self):
        i = 0
        while i < len(self.instructions):
            self.execute_instruction(self.instructions[i])
            offset = self.get_offset()

            if offset != 0:
                i += offset
            else:
                i += 1

    def execute_instruction(self, instruction):
        self.set_offset(0)

        # time.sleep(1)
        # print 'p{0} = {1} | {2}'.format(self.id, instruction, self.variables)

        command = instruction[0]
        variable = instruction[1]        
        variable_value = self.get_value(variable)

        param = None
        if len(instruction) > 2:
            try: 
                param = int(instruction[2])
            except ValueError:
                param = self.get_value(instruction[2])

        if command == 'set':
            self.set_value(variable, param)
        elif command == 'add':
            self.set_value(variable, variable_value + param)
        elif command == 'mul':
            self.set_value(variable, variable_value * param)
        elif command == 'mod':
            self.set_value(variable, variable_value % param)
        elif command == 'snd':
            self.send(variable)
        elif command == 'rcv':
            self.receive(variable)
        elif command == 'jgz':
            if not str(variable).isdigit:
                raise Exception('{0} is not a variable'.format(variable))

            if variable_value > 0:
                self.set_offset(param)
        else:
            raise Exception('Command "' + command + '" not implemented!')

    def get_value(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        else:
            try: 
                # jgz >> 1 << 3
                return int(variable)
            except ValueError:
                return 0
            

    def set_value(self, variable, value):
        self.variables[variable] = value

    def set_offset(self, offset):
        self.offset = offset

    def get_offset(self):
        return self.offset

    def link(self, program):
        if self.linked_program != program:
            self.linked_program = program
            program.link(self)


    def send(self, variable):
        self.linked_program.add_to_queue(self.get_value(variable))
        self.sending_count += 1

    def receive(self, variable):
        while True:
            if len(self.queue) == 0:
                if not self.waiting:
                    self.waiting = True
                    print 'Program {0} waiting... Messages send: #{1}'.format(self.id, self.sending_count)
            else:
                if self.waiting:
                    self.waiting = False
                    print 'Program {0} is back...'.format(self.id, self.sending_count)
                break

            if self.abort:
                return

        self.set_value(variable, self.queue.pop(0))

    def add_to_queue(self, value):
        self.queue.append(value)

    def stop(self):
        self.abort = True

    def to_string(self):
        return "|{0}|{1}|{2}|".format(self.id, self.variables, len(self.queue))

p0 = Program(0, instructions)
p1 = Program(1, instructions)

p0.link(p1)

p0.start()
p1.start()

# p0.waiting = True

while not (p0.waiting and p1.waiting):
    time.sleep(10)
    print p0.to_string()
    print p1.to_string()
    pass

p0.stop()
p1.stop()

print "Both programs are waiting"
print "Program 1 sending count is '{0}'".format(p1.sending_count)