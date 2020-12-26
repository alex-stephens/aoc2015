with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

tot = sum([len(x) for x in strings])
stored = 0

def ishex(string):
    for c in string: 
        if not (c.isdigit() or c in 'abcdef'):
            return False
    return True

for s in strings:
    c = s[1:-1]
    c = c.replace("\\\"", "\"")
    c = c.replace("\\\\", "\\")
    hexcount = 0

    for i in reversed(range(len(c))):
        if i <= len(c) - 4 and c[i:i+2] == '\\x' and ishex(c[i+2:i+4]):
            hexcount += 1

    stored += len(c) - hexcount * 3

print(tot - stored)