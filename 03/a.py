with open('input.txt') as f:
    line = f.readline()

dirs = {'^':(0,1), 'v':(0,-1), '<':(-1,0), '>':(1,0)}
pos = (0,0)
houses = {pos}

def update(pos, d):
    return (pos[0] + dirs[d][0], pos[1] + dirs[d][1])

for d in line:
    pos = update(pos, d)
    houses.add(pos)
print(len(houses))