N = int(input())
A = list(map(int, input().split()))

cum_top = [A[0]] + [0 for _ in range(N - 1)]
for i in range(1, N):
    cum_top[i] = max(cum_top[i - 1], A[i])

cum_back = [0 for _ in range(N - 1)] + [A[-1]]
for i in range(N - 2, -1, -1):
    cum_back[i] = max(cum_back[i + 1], A[i])

D = int(input())
for _ in range(D):
    l, r = map(int, input().split())
    print(max(cum_top[l - 2], cum_back[r]))
