with open('input.txt') as f:
    containers = list(map(int, [line.strip() for line in f.readlines()]))

# dp[V, N] = ways to make volume V using first N containers
V = 150             # volume
N = len(containers) # containers
dp = [[0 for _ in range(N+1)] for _ in range(V+1)]

for n in range(N+1):
    dp[0][n] = 1

for v in range(1, V+1):
    for n in range(1, N+1):
        dp[v][n] = dp[v][n-1]
        # print('yeet', dp[c][n])
        if containers[n-1] <= v:
            dp[v][n] += dp[v-containers[n-1]][n-1]

print(dp[-1][-1])
