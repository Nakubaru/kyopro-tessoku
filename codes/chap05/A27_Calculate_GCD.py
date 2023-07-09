def gcd(A: int, B: int) -> int:
    while A and B:
        if A >= B:
            A = A % B
        else:
            B = B % A

    return max(A, B)


A, B = map(int, input().split())
print(A * B // gcd(A, B))
