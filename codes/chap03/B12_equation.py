N = int(input())

left = 1.0
right = 100.0

for _ in range(30):
    mid = (left + right) / 2

    x = mid ** 3 + mid
    if x >= N:
        right = mid
    else:
        left = mid

print(mid)
