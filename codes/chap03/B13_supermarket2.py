N, K = map(int, input().split())
A = list(map(int, input().split()))

cum = [0] * (N + 1)
for i in range(1, N + 1):
    cum[i] = cum[i - 1] + A[i - 1]

R = [0] * N
for i in range(N):

    R[i] = -1 if i == 0 else R[i - 1]

    while R[i] < N - 1 and cum[R[i] + 2] - cum[i] <= K:
        R[i] += 1

print(sum(R[i] - i + 1 for i in range(N)))
