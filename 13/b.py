from itertools import permutations

with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

happiness, people = {}, set()

def parse(string):
    spl = string.split()
    p1, p2 = spl[0], spl[-1][:-1]
    people.add(p1)
    people.add(p2)

    if spl[2] == 'gain':
        sign = 1
    else:
        sign = -1

    happiness[(p1, p2)] = sign * int(spl[3])

def compute_happiness(p):
    ans = 0
    for i in range(len(p)):
        i2 = (i - 1) if i != 0 else len(p) - 1
        ans += happiness[(p[i], p[i2])]
        ans += happiness[(p[i2], p[i])]
    return ans

for s in strings:
    parse(s)
for p in people:
    happiness[("Me", p)] = 0
    happiness[(p, "Me")] = 0

people.add("Me")
people = list(people)
best = 0 

for p in permutations(people[1:]):
    p = [people[0]] + list(p)
    best = max(best, compute_happiness(p))
print(best)