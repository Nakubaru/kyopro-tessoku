N = input()
digit = len(N)

res = 0
for i, x in enumerate(N):
    res += 2 ** (digit - i - 1) * int(x)

print(res)
