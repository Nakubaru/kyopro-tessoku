N, K = map(int, input().split())
A, B = [0] * N, [0] * N

for i in range(N):
    a, b = map(int, input().split())
    A[i], B[i] = a, b

ans = 0
for a in range(1, 101):
    for b in range(1, 101):

        cnt = 0
        for i in range(N):
            if a <= A[i] <= a + K and b <= B[i] <= b + K:
                cnt += 1

        ans = max(ans, cnt)

print(ans)
