N, Q = map(int, input().split())
A = list(range(1, N + 1))

rev = False
for _ in range(Q):
    z, *xy = map(int, input().split())

    if z == 1:
        x, y = xy
        idx = N - x if rev else x - 1
        A[idx] = y

    elif z == 2:
        rev = not rev

    elif z == 3:
        x = xy[0]
        idx = N - x if rev else x - 1
        print(A[idx])
