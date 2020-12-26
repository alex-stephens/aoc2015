with open('input.txt') as f:
    strings = [line.strip() for line in f.readlines()]

orig = sum([len(x) for x in strings])
enc = 0

def ishex(string):
    for c in string: 
        if not (c.isdigit() or c in 'abcdef'):
            return False
    return True

for s in strings:
    c = c.replace("\\", "\\\\")
    c = c.replace("\"", "\\\"")
    c = "\"" + c + "\""
    enc += len(c)

print(enc - orig)