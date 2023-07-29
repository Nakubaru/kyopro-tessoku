import collections

Q = int(input())
que = collections.deque()

for _ in range(Q):
    q, *x = input().split()

    if q == '1':
        que.append(x[0])

    elif q == '2':
        print(que[0])

    elif q == '3':
        que.popleft()
