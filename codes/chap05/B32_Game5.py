N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [None] * (N + 1)

for i in range(N + 1):

    if any((i >= a and not dp[i - a]) for a in A):
        dp[i] = True

    else:
        dp[i] = False

print('First' if dp[N] else 'Second')
