N = int(input())

MAX = 1500
X = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    X[a][b] += 1
    X[a][d] -= 1
    X[c][b] -= 1
    X[c][d] += 1

for i in range(0, MAX + 1):
    for j in range(1, MAX + 1):
        X[i][j] = X[i][j-1] + X[i][j]

for i in range(1, MAX + 1):
    for j in range(0, MAX + 1):
        X[i][j] = X[i-1][j] + X[i][j]

print(sum(1 for xl in X for x in xl if x >= 1))
