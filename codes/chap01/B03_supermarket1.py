N = int(input())
A = list(map(int, input().split()))

for i, a_1 in enumerate(A):
    for j, a_2 in enumerate(A[i + 1:]):
        for a_3 in A[i + j + 2:]:

            if a_1 + a_2 + a_3 == 1000:
                print('Yes')
                break

        else:
            continue
        break

    else:
        continue
    break

else:
    print('No')
