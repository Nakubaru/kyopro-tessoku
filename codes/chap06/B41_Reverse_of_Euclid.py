X, Y = map(int, input().split())

ans = []
while not (X == 1 and Y == 1):
    ans.append((X, Y))
    if X >= Y:
        X -= Y
    else:
        Y -= X

print(len(ans))
for x, y in reversed(ans):
    print(x, y)
