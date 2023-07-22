N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
rows = {i: i for i in range(N)}

Q = int(input())
for _ in range(Q):
    z, x, y = map(int, input().split())

    if z == 1:
        rows[x - 1], rows[y - 1] = rows[y - 1], rows[x - 1]

    elif z == 2:
        print(A[rows[x - 1]][y - 1])
