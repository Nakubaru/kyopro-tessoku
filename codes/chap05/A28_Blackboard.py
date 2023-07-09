N = int(input())

A = [None] * (N + 1)
A[1], A[2] = 1, 1

for n in range(3, N + 1):
    A[n] = (A[n - 1] + A[n - 2]) % 1000000007

print(A[N])
