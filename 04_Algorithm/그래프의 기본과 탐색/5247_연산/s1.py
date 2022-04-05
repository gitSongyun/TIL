# 5247_연산
# 2022-04-01
import sys
sys.stdin = open('sample_input.txt')


def bfs(n):
    front = -1
    rear = 0
    visited = [0] * 1000001 # M+10
    queue = [n]


    # 중복을 없애기 위해 루트(N)를 visited 에 넣는다.
    visited[n] = 0

    while front <= rear:

        # n과 c를 꺼내고
        front += 1
        n = queue[front]
        # print(n)
        # n이 M에 도달하면 cnt 를 반환한다.
        if n == M:
            return visited[n]

        # for 문으로 작성해보기
        # 중복되지 않고, 범위 안에 들어오면
        if 0 <= n*2 <= 1000000 and not visited[n*2]:
            # 그 값과 카운트+1 한 다음 queue 에 담는다.
            queue.append(n*2)
            rear += 1
            # visited 에 값을 추가 한다.
            visited[n*2] = visited[n] + 1

        if 0 <= n+1 <= 1000000 and not visited[n+1]:
            queue.append(n+1)
            rear += 1
            visited[n+1] = visited[n] + 1

        if 0 <= n-1 <= 1000000 and not visited[n-1]:
            queue.append(n-1)
            rear += 1
            visited[n-1] = visited[n] + 1

        if 0 <= n-10 <= 1000000 and not visited[n-10]:
            queue.append(n-10)
            rear += 1
            visited[n-10] = visited[n] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, bfs(N)))


