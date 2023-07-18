import collections
import math

N = int(input())
A = list(map(int, input().split()))

cnt = collections.defaultdict(int)
for a in A:
    cnt[a] += 1

ans = 0
for v in cnt.values():
    ans += math.comb(v, 3)

print(ans)
