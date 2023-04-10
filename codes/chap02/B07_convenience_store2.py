T = int(input())
N = int(input())

ratio = [0] * (T + 1)
for _ in range(N):
    l, r = map(int, input().split())
    ratio[l] += 1
    ratio[r] -= 1

cum = 0
for i in range(T):
    cum = cum + ratio[i]
    print(cum)
