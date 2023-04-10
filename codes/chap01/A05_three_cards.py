N, K = map(int, input().split())

cnt = 0
for n1 in range(1, N + 1):
    for n2 in range(1, N + 1):

        n3 = K - n1 - n2
        if 0 < n3 <= N:
            cnt += 1

print(cnt)
