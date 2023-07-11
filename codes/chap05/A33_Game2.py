N = int(input())
A = list(map(int, input().split()))

xor = 0
for i in range(N):
    xor = xor ^ A[i]

print('First' if xor else 'Second')
