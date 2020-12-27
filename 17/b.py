with open('input.txt') as f:
    containers = list(map(int, [line.strip() for line in f.readlines()]))

# dp[V, N, C] = ways to make volume V using exactly C of the first N containers
V = 150             # volume
N = len(containers) # containers
C = len(containers) # max number of containers to use
dp = [[[0 for _ in range(C+1)] for _ in range(N+1)] for _ in range(V+1)]

for n in range(N+1):
    dp[0][n][0] = 1

for v in range(1, V+1):
    for n in range(1, N+1):
        for c in range(C+1):
            dp[v][n][c] = dp[v][n-1][c]
            # print('yeet', dp[c][n])
            if containers[n-1] <= v:
                dp[v][n][c] += dp[v-containers[n-1]][n-1][c-1]

for c in range(C+1):
    v = 150
    if dp[v][-1][c] > 0:
        ans = dp[v][-1][c]
        break

print(ans)