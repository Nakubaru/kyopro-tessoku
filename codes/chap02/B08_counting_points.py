MAX = 1500
N = int(input())
Z = [[0] * MAX for _ in range(MAX)]

for _ in range(N):
    x, y = map(int, input().split())
    Z[x - 1][y - 1] += 1

cum = [[0] * (MAX + 1) for _ in range(MAX + 1)]

# 横方向
for i in range(1, MAX + 1):
    for j in range(1, MAX + 1):
        cum[i][j] = cum[i][j - 1] + Z[i - 1][j - 1]

# 縦方向
for j in range(1, MAX + 1):
    for i in range(1, MAX + 1):
        cum[i][j] = cum[i - 1][j] + cum[i][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(cum[a - 1][b - 1] + cum[c][d] - cum[a - 1][d] - cum[c][b - 1])
