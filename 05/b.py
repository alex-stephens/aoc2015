import string

with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

letters = string.ascii_lowercase
pairs = [x+y for x in letters for y in letters]

def nice(s):
    c1, c2 = False, False
    for p in pairs: 
        if s.count(p) >= 2:
            c1 = True
            break
    for p in pairs: 
        if s.count(p + p[0]) >= 1:
            c2 = True
            break
    return c1 and c2

print(sum([nice(s) for s in strings]))