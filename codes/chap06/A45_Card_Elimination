N, C = input().split()
A = input()

score = sum(0 if a == 'W' else 1 if a == 'B' else 2 for a in A)
cond1 = score % 3 == 0 and C == 'W'
cond2 = score % 3 == 1 and C == 'B'
cond3 = score % 3 == 2 and C == 'R'

print('Yes' if cond1 or cond2 or cond3 else 'No')
