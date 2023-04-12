N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
goods = [dict(weight=wv[0], value=wv[1]) for wv in WV]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(W + 1):

        if j < goods[i - 1]['weight']:
            dp[i][j] = dp[i - 1][j]

        else:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i - 1][j - goods[i - 1]['weight']] + goods[i - 1]['value']
            )

print(max(dp[N]))
