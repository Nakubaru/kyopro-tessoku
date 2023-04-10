N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

cum = [{'win': 0, 'lose': 0}] + [dict() for _ in range(N)]

for i in range(1, N + 1):
    if A[i - 1]:
        cum[i]['win'] = cum[i - 1]['win'] + 1
        cum[i]['lose'] = cum[i - 1]['lose']
    else:
        cum[i]['win'] = cum[i - 1]['win']
        cum[i]['lose'] = cum[i - 1]['lose'] + 1

for lr in LR:
    win = cum[lr[1]]['win'] - cum[lr[0] - 1]['win']
    lose = cum[lr[1]]['lose'] - cum[lr[0] - 1]['lose']

    print('win' if win > lose else 'lose' if lose > win else 'draw')
