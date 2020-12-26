num = open('input.txt').readline()

def looksay(num):
    n = 1
    ans = ''
    for i in range(1,len(num)):
        if num[i] != num[i-1]:
            ans += str(n) + num[i-1]
            n = 1
        else:
            n += 1
    ans += str(n) + str(num[-1])
    return ans

iterations = 40
for i in range(iterations):
    num = looksay(num)

print(len(num))