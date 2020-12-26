with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

class Command(object):
    def __init__(self, cmd, ops, target, deps):
        self.cmd = cmd
        self.ops = ops
        self.target = target
        self.deps = deps

def bitwise(cmd, ops):

    for i, op in enumerate(ops):
        if type(op) == str:
            ops[i] = signals[op]

    if cmd == 'NOT':
        return 65535 - ops[0]
    if cmd == 'AND':
        return ops[0] & ops[1]
    elif cmd == 'OR':
        return ops[0] | ops[1]
    elif cmd == 'LSHIFT':
        return ops[0] << ops[1]
    elif cmd == 'RSHIFT':
        return ops[0] >> ops[1]
    elif cmd == 'SET':
        return ops[0]

def parse(s):
    ops, target = s.split(' -> ')

    if ops.startswith('NOT'):
        cmd = 'NOT'
        ops = [ops.split()[1]]

    elif ops.find('AND') != -1:
        cmd = 'AND'
        ops = ops.split(' AND ')

    elif ops.find('OR') != -1:
        cmd = 'OR'
        ops = ops.split(' OR ')

    elif ops.find('LSHIFT') != -1:
        cmd = 'LSHIFT'
        ops = ops.split(' LSHIFT ')

    elif ops.find('RSHIFT') != -1:
        cmd = 'RSHIFT'
        ops = ops.split(' RSHIFT ')

    else:
        cmd = 'SET'
        ops = [ops]

    deps = []

    for i, op in enumerate(ops):
        if op[0].isdigit():
            ops[i] = int(op)
        else:
            deps.append(op)

    return cmd, ops, target, deps

signals = {}

def execute(strings):
    todo, done = [], set()

    for s in strings:
        cmd, ops, target, deps = parse(s)
        todo.append(Command(cmd, ops, target, deps))

    while len(todo) > 0:
        for i in reversed(range(len(todo))):
            c = todo[i]
            possible = True
            for d in c.deps:
                if d not in done:
                    possible = False
                    break
            if possible:
                output = bitwise(c.cmd, c.ops)
                signals[c.target] = output
                todo.pop(i)
                done.add(c.target)

execute(strings)
print(signals['a'])
    