with open('input.txt') as f:
    inst = f.readline().strip()
print(inst.count('(') - inst.count(')'))