import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 1일 때에는 무조건 1만 출력되기 때문에 기본값으로 리스트 초기화
    res = [1]

    # 예쁜 트리 출력을 위해 테스트케이스와 1일때를 먼저 출력
    print('#{}'.format(tc))
    print(*res)

    # 2번째줄부터 시작해서 총 범위는 N - 1 가 됨
    for i in range(N - 1):
        # 테두리는 항상 1 임
        stack = [0] + res + [0]
        res = []

        # 오른쪽 위 값
        num = stack.pop()

        while stack:
            # 왼쪽 위 값
            num2 = stack.pop()
            # 오른쪽 위와 왼쪽 위를 합침
            res.append(num + num2)
            # 오른쪽을 왼쪽으로 넘겨줌
            num = num2

        print(*res)




