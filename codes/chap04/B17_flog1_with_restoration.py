N = int(input())
H = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(H[1] - H[0])

for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]),
                dp[i - 2] + abs(H[i] - H[i - 2]))

current = N - 1
result = [current + 1]

while current > 0:
    if dp[current] == dp[current - 1] + abs(H[current] - H[current - 1]):
        current -= 1
    else:
        current -= 2

    result.append(current + 1)

print(len(result))
print(' '.join(map(str, reversed(result))))
