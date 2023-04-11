N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 1
right = 10 ** 9

while left < right:
    mid = (left + right) // 2

    num = sum(mid // A[i] for i in range(N))
    if num >= K:
        right = mid
    else:
        left = mid + 1

print(left)
