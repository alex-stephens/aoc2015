with open('input.txt') as f:
    inst = f.readline().strip()

floor = 0
for i, c in enumerate(inst):
    floor += 1 if c == '(' else -1
    if floor == -1:
        break
print(i+1)
