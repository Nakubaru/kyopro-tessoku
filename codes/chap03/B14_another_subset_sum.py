import bisect
import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

A_top, A_back = A[:N // 2], A[N // 2:]
sum_top, sum_back = [], []

for bits in itertools.product((0, 1), repeat=len(A_top)):
    sum_top.append(sum(A_top[i] for i in range(len(A_top)) if bits[i]))

for bits in itertools.product((0, 1), repeat=len(A_back)):
    sum_back.append(sum(A_back[i] for i in range(len(A_back)) if bits[i]))

sum_back.sort()

for x in sum_top:
    idx = bisect.bisect_left(sum_back, K - x)

    if idx < len(sum_back) and sum_back[idx] == K - x:
        print('Yes')
        break

else:
    print('No')
