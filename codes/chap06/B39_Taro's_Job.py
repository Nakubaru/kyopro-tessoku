import heapq

N, D = map(int, input().split())

XY = {i: [] for i in range(1, D + 1)}
for i in range(N):
    x, y = map(int, input().split())
    XY[x].append(y)

q, ans = [], 0
for day in range(1, D + 1):

    for y in XY[day]:
        heapq.heappush(q, -y)

    if q:
        ans -= heapq.heappop(q)

print(ans)
