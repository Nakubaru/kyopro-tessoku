N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0] * N
for i in range(N - 1):
    R[i] = 0 if i == 0 else R[i - 1]

    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

print(sum(R[i] - i for i in range(N - 1)))
