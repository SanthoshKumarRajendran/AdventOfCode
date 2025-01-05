INPUTS = {}
CONNECTIONS = {}
OP_MAP = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b
}

class Gate:
    def __init__(self, var_1, var_2, op):
        self.var_1 = var_1
        self.var_2 = var_2
        self.op = OP_MAP[op]

    def evaluate(self):
        if self.var_1 not in INPUTS:
            INPUTS[self.var_1] = CONNECTIONS[self.var_1].evaluate()
        if self.var_2 not in INPUTS:
            INPUTS[self.var_2] = CONNECTIONS[self.var_2].evaluate()
        return self.op(INPUTS[self.var_1], INPUTS[self.var_2])

with open('input.txt', 'r') as f:
    for line in f:
        if ': ' in line:
            var, val = line.strip().split(': ')
            val = True if val == '1' else False
            INPUTS[var] = val
        if ' -> ' in line:
            var_1, op, var_2, _, out = line.strip().split(' ')
            CONNECTIONS[out] = Gate(var_1, var_2, op)

# print(CONNECTIONS)

OUTPUT = ''
for key in sorted(CONNECTIONS.keys(), reverse=True):
    if not key.startswith('z'):
        continue
    OUTPUT += '1' if CONNECTIONS[key].evaluate() else '0'

print(OUTPUT)
print(int(OUTPUT, base=2))
