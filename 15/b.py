from itertools import combinations

with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

class Ingredient(object):
    def __init__(self, string):
        spl = string.split()
        self.name = spl[0][:-1]
        self.capacity = int(spl[2][:-1])
        self.durability = int(spl[4][:-1])
        self.flavor = int(spl[6][:-1])
        self.texture = int(spl[8][:-1])
        self.calories = int(spl[10])
        
ings = [Ingredient(s) for s in strings]

def quantities(q, n):
    qty = [0] * (len(q) + 1)
    qty[0] = q[0]
    for i in range(1,len(q)):
        qty[i] = q[i] - q[i-1]
    qty[-1] = n - q[-1]
    return qty

def score(ings, qty):
    metrics, calories = [0, 0, 0, 0], 0
    for i in range(len(qty)):
        metrics[0] += qty[i] * ings[i].capacity
        metrics[1] += qty[i] * ings[i].durability
        metrics[2] += qty[i] * ings[i].flavor
        metrics[3] += qty[i] * ings[i].texture
        calories   += qty[i] * ings[i].calories

    sc = 1
    for i in range(4): 
        sc *= max(metrics[i], 0)
    return sc, calories

n = len(ings)
tot, best = 100, 0

for q in combinations(range(tot+1), n-1):
    qty = quantities(q, tot)
    s, cal = score(ings, qty)
    # print(s, cal)
    if cal == 500:
        best = max(best, s)
print(best)