# 1232_사칙연산
# 2022-03-17
import sys
sys.stdin = open('input.txt')

# 후위 순회
def post_order(v):
    if v: # 루트 노드
        post_order(ch1[v])
        post_order(ch2[v])

        # 숫자면 스택에 담고
        # 문자를 만나면 연산을 한다.
        if str(tree[v]).isdigit():
            stack.append(tree[v])

        if tree[v] in op:
            if tree[v] == '-':
                a = stack.pop(-1)
                b = stack.pop(-1)
                tree[v] = b - a
                stack.append(tree[v])

            elif tree[v] == '+':
                a = stack.pop(-1)
                b = stack.pop(-1)
                tree[v] = b + a
                stack.append(tree[v])

            elif tree[v] == '*':
                a = stack.pop(-1)
                b = stack.pop(-1)
                tree[v] = b * a
                stack.append(tree[v])

            elif tree[v] == '/':
                a = stack.pop(-1)
                b = stack.pop(-1)
                tree[v] = b / a
                stack.append(tree[v])

    # 최종 연산된 값이 stack 에 들어가게 된다.
    return stack

T = 10
for tc in range(1, T+1):

    N = int(input())                 # 노드의 갯수
    op = ['+', '-', '*', '/']        # 연산자 리스트

    tree = [[] for _ in range(N+1)]  # 트리 구조
    ch1 = [[] for _ in range(N+1)]   # 왼쪽 자식
    ch2 = [[] for _ in range(N+1)]   # 오른쪽 자식

    # 계산 결과를 담을 stack
    stack = []

    # arr = [부모 노드 번호, 연산자 or 숫자, 왼쪽 자식 노드 번호, 오른쪽 자식 노드 번호]
    for _ in range(N):
        arr = list(map(str, input().split()))

        # arr 의 길이가 4라면 자식 노드번호가 담겨 있다.
        if len(arr) == 4:
            tree[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])

        # 그렇지 않다면 자식이 없는 노드
        else:
            tree[int(arr[0])] = int(arr[1])


    result = post_order(1)

    print("#{} {}".format(tc, int(result[0])))

