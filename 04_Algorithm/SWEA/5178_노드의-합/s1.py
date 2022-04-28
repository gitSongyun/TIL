import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 노드의 갯수 M: 리프 노드의 갯수 T: 출력할 노드 번호
    N, M, T = list(map(int, input().split()))

    tree = [0]*(N+1)

    for _ in range(M):
        idx, num = list(map(int,input().split()))

        tree[idx] = num


    for i in range(N, 0, -1):
        tree[i//2] += tree[i]

    print("#{} {}".format(tc, tree[T]))
