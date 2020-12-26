from itertools import permutations

with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

distance, places = {}, set()

def parse(s):
    places, dist = s.split(" = ")
    dist = int(dist)
    a, b = places.split(" to ")
    return a, b, dist
    
def path(p):
    return sum([distance[(p[i-1],p[i])] for i in range(1,len(p))])

for s in strings:
    a, b, dist = parse(s)
    places.add(a)
    places.add(b)
    distance[(a,b)] = dist
    distance[(b,a)] = dist

print(max([path(p) for p in permutations(places)]))