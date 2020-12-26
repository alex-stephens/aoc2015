instructions = []
with open('input.txt') as f:
    for line in f.readlines():
        instructions.append(line.strip()) 

def parse(instruction):
    if instruction.startswith('toggle'):
        cmd = 0 # toggle
    elif instruction.startswith('turn on'):
        cmd = 1 # on
    else: 
        cmd = 2 # off

    p1 = instruction.split()[-3]
    p1 = tuple(map(int, p1.split(',')))
    p2 = instruction.split()[-1]
    p2 = tuple(map(int, p2.split(',')))

    return cmd, p1, p2

size = 1000
lights = [[0 for _ in range(size)] for _ in range(size)]

def apply(cmd, p1, p2):
    for r in range(p1[0], p2[0]+1):
        for c in range(p1[1], p2[1]+1):
            if cmd == 0:
                lights[r][c] = 1 - lights[r][c]
            elif cmd == 1:
                lights[r][c] = 1
            else:
                lights[r][c] = 0

for i in instructions:
    cmd, p1, p2 = parse(i)
    apply(cmd, p1, p2)

print(sum([sum(x) for x in lights]))
