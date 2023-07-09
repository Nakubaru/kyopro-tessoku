def ncr(n: int, r: int, mod: int):
    a = 1
    for i in range(1, n + 1):
        a = a * i % mod

    b = 1
    for i in range(1, r + 1):
        b = b * i % mod
    for i in range(1, n - r + 1):
        b = b * i % mod

    return a * pow(b, mod - 2, mod) % mod


a, b = map(int, input().split())
print(ncr(a, b, 1000000007))
