N, Q = map(int, input().split())
A = list(map(int, input().split()))

LR = [None] * Q
for i in range(Q):
    L, R = map(int, input().split())
    LR[i] = (L, R)

cum = [0] + [None] * N
for i in range(1, N + 1):
    cum[i] = cum[i - 1] + A[i - 1]

for lr in LR:
    print(cum[lr[1]] - cum[lr[0] - 1])
