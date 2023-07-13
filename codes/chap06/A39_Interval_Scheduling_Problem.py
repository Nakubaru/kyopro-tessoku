N = int(input())

LR = [None] * N
for i in range(N):
    left, right = map(int, input().split())
    LR[i] = (left, right)

cnt, current = 0, 0
for left, right in sorted(LR, key=lambda x: x[1]):
    if left >= current:
        current = right
        cnt += 1

print(cnt)
