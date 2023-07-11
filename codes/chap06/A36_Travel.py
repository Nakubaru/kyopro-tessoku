N, K = map(int, input().split())
print('Yes' if K >= N * 2 - 2 and K % 2 == 0 else 'No')
