D, N = map(int, input().split())
time = [24] * D

for _ in range(N):
    L, R, H = map(int, input().split())

    for t in range(L - 1, R):
        time[t] = min(H, time[t])

print(sum(time))
