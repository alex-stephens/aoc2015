with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

class Reindeer(object):
    def __init__(self, string):
        spl = string.split()
        self.name = spl[0]
        self.speed = int(spl[3])
        self.time = int(spl[6])
        self.rest = int(spl[-2])

reindeer = []

for s in strings:
    reindeer.append(Reindeer(s))
    d = reindeer[-1]

def travelled(r, t):
    cycle = r.time + r.rest
    full_cycles = t // cycle
    extra = min(t % cycle, r.time)
    return (r.time * full_cycles + extra) * r.speed

t = 2503
print(max([travelled(r,t) for r in reindeer]))