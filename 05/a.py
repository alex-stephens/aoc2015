with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

def nice(s):
    vowels = sum([s.count(x) for x in 'aeiou'])
    double = any([s[i-1]==s[i] for i in range(1,len(s))])
    forbidden = any([s.find(x) != -1 for x in ('ab', 'cd', 'pq', 'xy')])
    return vowels >= 3 and double and not forbidden

print(sum([nice(s) for s in strings]))