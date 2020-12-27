import json

def recursive_sum(s):
    val = 0
    if type(s) == int:
        val += s
    elif type(s) == dict:
        val += sum([recursive_sum(s[k]) for k in s.keys()])
    elif type(s) == list:
        val += sum([recursive_sum(x) for x in s])
    return val

s = open('input.txt').readline()
s = json.loads(s)
print(recursive_sum(s))