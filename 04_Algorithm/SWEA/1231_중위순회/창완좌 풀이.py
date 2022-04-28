import sys
sys.stdin = open('input.txt', 'r')


# 중위순회
def in_order(T):
    if T <= N:
        in_order(T*2)
        print(tree[T], end='')
        in_order(T*2 + 1)


T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for n in range(N):
        N_lst = list(map(str, input().split()))
        tree[int(N_lst[0])] = N_lst[1]
        print(tree)

    # print('#{}'.format(tc), end=' ')
    in_order(1)
    print()