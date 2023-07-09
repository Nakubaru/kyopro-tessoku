A, B = map(int, input().split())

while A and B:
    if A >= B:
        A = A % B
    else:
        B = B % A

print(max(A, B))
