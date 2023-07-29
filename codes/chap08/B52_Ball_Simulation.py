import collections

N, X = map(int, input().split())
A = list(input())

q = collections.deque([X - 1])
A[X - 1] = '@'

while q:
    pos = q.popleft()

    if pos > 0 and A[pos - 1] == '.':
        A[pos - 1] = '@'
        q.append(pos - 1)

    if pos < N - 1 and A[pos + 1] == '.':
        A[pos + 1] = '@'
        q.append(pos + 1)

print(''.join(A))
