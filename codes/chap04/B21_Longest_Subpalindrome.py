N = int(input())
S = input()

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

    try:
        dp[i][i + 1] = 2 if S[i] == S[i + 1] else 1

    # i = N
    except IndexError:
        pass

for l_r in range(2, N):
    for left in range(N - l_r):
        r = left + l_r

        dp[left][r] = max(
            dp[left][r - 1],
            dp[left + 1][r],
            dp[left + 1][r - 1] + 2 if S[left] == S[r] else 0
        )

print(dp[0][N - 1])
