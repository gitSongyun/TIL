import sys
sys.stdin = open('input.txt')

T = 1

# 중위 순회 함수
def IN_ORDER(v):
    # v = 현재노드
    if v <= N:
        # 왼쪽 트리를 쭉 탐색 후 루트 노드로 돌아온다.
        IN_ORDER(v*2)
        print(arr[v], end='')
        # 오른쪽 노드를 탐색한다.
        IN_ORDER(v*2 + 1)

for tc in range(1, T+1):
    N = int(input())  # 노드 갯수

    # 노드 번호와 알파벳이 담긴 input 리스트
    tree = [list(map(str, input().split())) for _ in range(N)]

    # 입력을 노드 번호에 맞게 알파벳을 넣을 리스트
    arr = [[] for _ in range(N+1)]

    # 해당 노드에 알파벳을 넣는다.
    for i in tree:
        arr[int(i[0])] = i[1]

    print("#{}".format(tc), end=' ')
    IN_ORDER(1)
    print()
