N, A, B = map(int, input().split())
dp = [None] * (N + 1)

for i in range(N + 1):

    if (i >= A and not dp[i - A]) or (i >= B and not dp[i - B]):
        dp[i] = True

    else:
        dp[i] = False

print('First' if dp[N] else 'Second')
