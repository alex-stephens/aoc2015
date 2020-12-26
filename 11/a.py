from string import ascii_lowercase

s = open('input.txt').readline()
seq = {ascii_lowercase[i-2:i+1] for i in range(2, len(ascii_lowercase))}

def valid(s):
    forbidden = 'iol'
    for c in forbidden:
        if s.find(c) != -1:
            return False

    valid = False
    for asc in seq: 
        if s.find(asc) != -1:
            valid = True 
            break
    if not valid:
        return False

    paired = None
    for i in range(1,len(s)):
        if s[i] == s[i-1]: 
            if not paired: 
                paired = s[i]
            elif paired != s[i]:
                return True

    return False

def increment(s):
    s = list(s)
    i = len(s) - 1

    while True:
        if s[i] == 'z':
            s[i] = 'a'
            i -= 1
        else:
            s[i] = chr(ord(s[i]) + 1)
            break

    return ''.join(s)

while not valid(s):
    s = increment(s)

print(s)