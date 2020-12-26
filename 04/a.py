import hashlib 
key = open('input.txt').readline()

def check(key, num):
    string = key + str(num)
    hash = hashlib.md5(string.encode())
    result = hash.hexdigest()
    nzeros = 5
    return result.startswith('0'*nzeros)

n = 0
while True:
    if check(key, n):
        break
    n += 1
print(n)