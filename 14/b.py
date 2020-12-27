with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

class Reindeer(object):
    def __init__(self, string):
        spl = string.split()
        self.name = spl[0]
        self.speed = int(spl[3])
        self.time = int(spl[6])
        self.rest = int(spl[-2])

        self.rem_rest = 0
        self.burst = 0
        self.pos = 0
        self.points = 0

    def move(self):
        if self.burst == self.time:
            self.burst = 0
            self.rem_rest = self.rest - 1
        elif self.rem_rest > 0:
            self.rem_rest -= 1
        elif self.rem_rest == 0:
            self.burst += 1
            self.pos += self.speed

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
lead = 0

for _ in range(t):
    for r in reindeer:
        r.move()
        lead = max(lead, r.pos)

    for r in reindeer:
        r.points += 1 if r.pos == lead else 0 

print(max([r.points for r in reindeer]))