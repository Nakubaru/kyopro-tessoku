N, H, W = map(int, input().split())

xor = 0
for i in range(N):
    a, b = map(int, input().split())
    xor = xor ^ (a - 1)
    xor = xor ^ (b - 1)

print('First' if xor else 'Second')
