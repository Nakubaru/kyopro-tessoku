D = int(input())
N = int(input())

ratio = [0] * (D + 1)
for _ in range(N):
    l, r = map(int, input().split())
    ratio[l - 1] += 1
    ratio[r] -= 1

cum = 0
for i in range(D):
    cum = cum + ratio[i]
    print(cum)
