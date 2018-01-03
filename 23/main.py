import sys

instructions = list(open('23\input.txt').readlines())
instructions = map(lambda i: i.strip().split(' '), instructions)

class Processor():

    def __init__(self):
        self.variables = {}
        self.mul_invoked = 0

    def process(self, instructions):
        i = 0
        while i < len(instructions):
            self.process_instruction(instructions[i])
            offset = self.get_offset()

            if offset != 0:
                i += offset
            else:
                i += 1

    def process_instruction(self, instruction):
        if self.validate_condition(instruction):
            self.execute_instruction(instruction)
    
    def validate_condition(self, condition):
        return True

    def execute_instruction(self, instruction):
        # print "$ {0} | vars: {1} | mul_invoked: {2}".format(instruction, self.variables, self.mul_invoked)

        self.set_offset(0)

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
        elif command == 'sub':
            self.set_value(variable, variable_value - param)
        elif command == 'mul':
            self.set_value(variable, variable_value * param)
            self.mul_invoked += 1
        elif command == 'jnz':
            if variable_value != 0:
                self.set_offset(param)
        else:
            raise Exception('Command "' + command + '" not implemented!')

    def get_value(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        else:
            # in case it is a number and not a variable
            try: 
                return int(variable)
            except ValueError:
                return 0

    def set_value(self, variable, value):
        self.variables[variable] = value

    def set_offset(self, offset):
        self.set_value('offset', offset)
        if offset != 0:
            pass
            #print "Offset set to '{0}'.".format(offset)

    def get_offset(self):
        return self.get_value('offset')

p = Processor()
p.process(instructions)
print p.mul_invoked