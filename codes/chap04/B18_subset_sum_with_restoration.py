N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):

        if j < A[i - 1]:
            if dp[i - 1][j]:
                dp[i][j] = True

        elif j >= A[i - 1]:
            if dp[i - 1][j] or dp[i - 1][j - A[i - 1]]:
                dp[i][j] = True

if dp[N][S]:
    s, result = S, []
    for i in reversed(range(1, N + 1)):

        if dp[i - 1][s]:
            continue

        else:
            s -= A[i - 1]
            result.append(i)

    print(len(result))
    print(' '.join(map(str, reversed(result))))

else:
    print(-1)
