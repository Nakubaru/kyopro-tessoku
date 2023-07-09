N = int(input())

ans = 0
for _ in range(N):
    t, a = input().split()
    ans = eval(f'{ans} {t} {int(a)}')

    if ans < 0:
        ans += 10000

    ans %= 10000

    print(ans)
