import heapq

Q = int(input())

q = []
for _ in range(Q):
    y, *x = input().split()

    if y == '1':
        heapq.heappush(q, int(x[0]))

    elif y == '2':
        print(q[0])

    elif y == '3':
        heapq.heappop(q)
