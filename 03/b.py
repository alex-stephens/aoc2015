with open('input.txt') as f:
    line = f.readline()

dirs = {'^':(0,1), 'v':(0,-1), '<':(-1,0), '>':(1,0)}
p1, p2 = (0,0), (0,0)
houses = {p1}

def update(pos, d):
    return (pos[0] + dirs[d][0], pos[1] + dirs[d][1])

for i, d in enumerate(line):
    if i % 2 == 0:
        p1 = update(p1, d)
        houses.add(p1)
    else: 
        p2 = update(p2, d)
        houses.add(p2)

print(len(houses))