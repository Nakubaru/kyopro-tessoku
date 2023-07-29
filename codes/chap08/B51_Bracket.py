import collections

S = input()

op = collections.deque()

for i, s in enumerate(S):
    if s == '(':
        op.append(i + 1)

    elif s == ')':
        print(op.pop(), i + 1)
