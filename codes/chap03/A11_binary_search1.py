N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = len(A) - 1

while True:
    mid = (left + right) // 2

    if A[mid] == X:
        break
    elif A[mid] > X:
        right = mid - 1
    else:
        left = mid + 1

print(mid + 1)
