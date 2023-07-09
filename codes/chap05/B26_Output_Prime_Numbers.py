def eratostenes(N: int) -> list:
    is_prime = [False, False] + [True] * (N - 1)

    for p in range(2, N + 1):
        if not is_prime[p]:
            continue

        for q in range(p * 2, N + 1, p):
            is_prime[q] = False

    return [i for i, p in enumerate(is_prime) if p]


N = int(input())
for x in eratostenes(N=N):
    print(x)
