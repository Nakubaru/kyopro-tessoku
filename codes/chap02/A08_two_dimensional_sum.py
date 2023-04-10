H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

cum = [[0] * (W + 1) for _ in range(H + 1)]

# 横方向
for i in range(1, H + 1):
    for j in range(1, W + 1):
        cum[i][j] = cum[i][j - 1] + X[i - 1][j - 1]

# 縦方向
for j in range(1, W + 1):
    for i in range(1, H + 1):
        cum[i][j] = cum[i - 1][j] + cum[i][j]

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(cum[A - 1][B - 1] + cum[C][D] - cum[A - 1][D] - cum[C][B - 1])
