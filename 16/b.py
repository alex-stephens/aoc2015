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
        if prop == 'cats' and val <= true['cats']:
            sues[n] = False
        if prop == 'trees' and val <= true['trees']:
            sues[n] = False
        if prop == 'pomeranians' and val >= true['pomeranians']:
            sues[n] = False
        if prop == 'goldfish' and val >= true['goldfish']:
            sues[n] = False

        if prop not in ('cats', 'trees', 'pomeranians', 'goldfish') and true[prop] != val: 
            sues[n] = False
        
        if not sues[n]:
            break
    if sues[n]:
        break

print(n)