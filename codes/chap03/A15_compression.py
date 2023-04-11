import bisect

N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(set(A))

result = [bisect.bisect_left(A_sorted, A[i]) + 1 for i in range(N)]
print(' '.join(map(str, result)))
