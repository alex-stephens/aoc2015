grid = [list(line.strip()) for line in open('input.txt').readlines()]
rows, cols = len(grid), len(grid[0])

def count_neighbours(i, j):
    rmin, rmax = max(i-1, 0), min(i+1, rows-1)
    cmin, cmax = max(j-1, 0), min(j+1, cols-1)

    ans = 0 
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if (r,c) == (i,j):
                continue
            ans += 1 if grid[r][c] == '#' else 0
    return ans

it = 100

for i in range(it):
    new_grid = [['x' for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            count = count_neighbours(r,c)
            if grid[r][c] == '#' and (count != 2 and count != 3):
                new_grid[r][c] = '.'
            elif grid[r][c] == '.' and count == 3:
                new_grid[r][c] = '#'
            else:
                new_grid[r][c] = grid[r][c]

    grid = [list(x) for x in new_grid]
    # print('--------------------------')
    # for g in grid:
    #     print(''.join(g))

print(sum([''.join(r).count('#') for r in grid]))