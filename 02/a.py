def calc_paper(dims):
    l, w, h = sorted(dims)
    return 2*(l*w + l*h + w*h) + l*w

ans = 0

with open('input.txt') as f:
    for line in f.readlines():
        dims = list(map(int, line.split('x')))
        ans += calc_paper(dims)
print(ans)
