N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[1] = A[0]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

current = N - 1
result = [current + 1]

while current > 0:

    if dp[current] == dp[current - 1] + A[current - 1]:
        current -= 1
    else:
        current -= 2

    result.append(current + 1)

print(len(result))
print(' '.join(map(str, reversed(result))))
