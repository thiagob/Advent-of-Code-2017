instructions = list(open('08\input.txt').readlines())
instructions = map(lambda i: i.replace('\n','').split(' if '), instructions)

class Processor():

    def __init__(self):
        self.variables = {}
        self.max_value = 0

    def process(self, instructions):
        for instruction in instructions:
            self.process_instruction(instruction)

    def process_instruction(self, instruction):
        if self.validate_condition(instruction[1]):
            self.execute_instruction(instruction[0])
    
    def validate_condition(self, condition):
        parts = condition.split(' ')

        variable = parts[0]
        operator = parts[1]
        amount = int(parts[2])

        value = self.get_value(variable)

        if operator == '>':
            return value > amount
        elif operator == '<':
            return value < amount
        elif operator == '>=':
            return value >= amount
        elif operator == '<=':
            return value <= amount
        elif operator == '==':
            return value == amount
        elif operator == '!=':
            return value != amount
        else:
            raise Exception('Operator "' + operator + '" not implemented!')

    def execute_instruction(self, instruction):
        parts = instruction.split(' ')

        variable = parts[0]
        operator = parts[1]
        amount = int(parts[2])

        value = self.get_value(variable)

        if operator == 'inc':
            self.set_value(variable, value + amount)
        elif operator == 'dec':
            self.set_value(variable, value - amount)
        else:
            raise Exception('Operator "' + operator + '" not implemented!')

    def get_value(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        else:
            return 0

    def set_value(self, variable, value):
        self.variables[variable] = value
        if value > self.max_value:
            self.max_value = value

    def get_largest_variable(self):
        return max(p.variables.values())

p = Processor()
p.process(instructions)
print p.variables
print p.get_largest_variable()
print p.max_value