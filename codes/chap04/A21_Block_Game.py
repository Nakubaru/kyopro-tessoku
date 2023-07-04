N = int(input())

P, A = [0] * N, [0] * N
for i in range(N):
    P[i], A[i] = map(int, input().split())

dp = [[0] * N for _ in range(N)]

# r_left = r - left
for r_l in range(N - 1)[::-1]:
    for left in range(N - r_l):
        r = left + r_l

        if left > 0:
            dp[left][r] = \
                dp[left - 1][r] + A[left - 1] * (left <= P[left - 1] - 1 <= r)

        if r < N - 1:
            dp[left][r] = max(
                dp[left][r],
                dp[left][r + 1] + A[r + 1] * (left <= P[r + 1] - 1 <= r)
            )

print(max(map(max, dp)))
