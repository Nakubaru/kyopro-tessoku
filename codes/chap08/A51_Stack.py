import collections

Q = int(input())
st = collections.deque()

for _ in range(Q):
    q, *x = input().split()

    if q == '1':
        st.append(x[0])

    elif q == '2':
        print(st[-1])

    elif q == '3':
        st.pop()
