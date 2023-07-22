N, L = map(int, input().split())

ans = 0
for _ in range(N):
    a, b = input().split()
    time = L - int(a) if b == 'E' else int(a)
    ans = max(ans, time)

print(ans)
