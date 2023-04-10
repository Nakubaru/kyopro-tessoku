H, W, N = map(int, input().split())
kingdom = [[0] * (W + 2) for _ in range(H + 2)]
cum = [[0] * (W + 2) for _ in range(H + 2)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    kingdom[a][b] += 1
    kingdom[c + 1][d + 1] += 1
    kingdom[a][d + 1] -= 1
    kingdom[c + 1][b] -= 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        cum[i][j] = cum[i][j - 1] + kingdom[i][j]

for j in range(1, W + 1):
    for i in range(1, H + 1):
        cum[i][j] = cum[i - 1][j] + cum[i][j]

for c in cum[1:-1]:
    print(' '.join([str(x) for x in c[1:-1]]))
