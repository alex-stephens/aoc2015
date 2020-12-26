def calc_ribbon(dims):
    l, w, h = sorted(dims)
    return 2*(l+w) + l*w*h

ans = 0

with open('input.txt') as f:
    for line in f.readlines():
        dims = list(map(int, line.split('x')))
        ans += calc_ribbon(dims)
print(ans)
