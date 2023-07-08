N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

inf = float('inf')
dp = [[inf] * (2 ** N) for _ in range(M + 1)]
dp[0][0] = 0

for i in range(1, M + 1):
    for j in range(2 ** N):

        already = [None] * N
        for k in range(N):
            already[k] = 1 if j & 1 << k else 0

    v = 0
    for k in range(N):
        if already[k] or A[i - 1][k]:
            v += 2 ** k

    dp[i][j] = min(dp[i][j], dp[i - 1][j])
    dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

print(-1 if dp[M][-1] == inf else dp[M][-1])
