import collections
import heapq

N, D = map(int, input().split())

works = collections.defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    works[x].append(-y)

q, ans = [], 0
for i in range(1, D + 1):
    for w in works[i]:
        heapq.heappush(q, w)

    if q:
        ans -= heapq.heappop(q)

print(ans)
