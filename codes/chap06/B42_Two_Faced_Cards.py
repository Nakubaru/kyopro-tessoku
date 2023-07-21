def solve(N: int, A: list, B: list, pos_front: bool, pos_back: bool) -> int:
    cnt = 0
    for i in range(N):
        front = A[i] if pos_front else -A[i]
        back = B[i] if pos_back else -B[i]

        if front + back >= 0:
            cnt += front + back

    return cnt


N = int(input())
A, B = [0] * N, [0] * N

for i in range(N):
    a, b = map(int, input().split())
    A[i], B[i] = a, b

ans1 = solve(N=N, A=A, B=B, pos_front=True, pos_back=True)
ans2 = solve(N=N, A=A, B=B, pos_front=True, pos_back=False)
ans3 = solve(N=N, A=A, B=B, pos_front=False, pos_back=True)
ans4 = solve(N=N, A=A, B=B, pos_front=False, pos_back=False)

print(max(ans1, ans2, ans3, ans4))
