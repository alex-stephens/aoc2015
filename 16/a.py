with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

true = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, \
    'vizslas':0, 'goldfish':5, 'trees': 3, 'cars': 2, 'perfumes': 1}
sues = [True] * 501

for s in strings:
    spl = s.split()
    n = int(spl[1][:-1])
    for j in range(2, len(spl), 2):
        prop = spl[j][:-1]
        val = int(spl[j+1].strip(','))
        if true[prop] != val: 
            sues[n] = False
            continue
    if sues[n]:
        break

print(n)