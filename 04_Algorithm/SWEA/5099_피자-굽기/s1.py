import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def FIRE(n, idx):

    # 화덕의 크기만큼 번호가 적힌 피자들을 넣는다.
    for i in range(n):
        queue.append(idx[i])

    k = 1
    while queue:

        # 화덕의 크기 만큼 반복문 돌린다.
        for i in range(N):
            if len(queue) == 0:
                break
            # 이 때 자리를 한칸씩 밀어낸다.
            temp = queue.pop(0)

            # 0번 인덱스(화덕입구)에 치즈가 0이 되는 피자가 왔을 때,
            if ch[temp] == 0:
                # 남은 피자가 있다면 그 자리에 새로운 피자를 넣는다.
                if n+k-1 < M: # n =3 k =1  => 3번 피자가 새로들어간다.
                    queue.append(idx[n+k-1])
                    k += 1
            else:
                queue.append(temp)
        # 문제점
        # 순서 상관없이 처음부터 시작한다
        # 반복문이 다 돌면 화덕안 피자의 치즈를 2로 나누고 다시 돌린다.
        for j in queue:
            ch[j] = ch[j]//2

    print(temp + 1)


for tc in range(1, T+1):
    # N : 화덕의 크기, M : 피자의 갯수
    N, M = list(map(int, input().split()))

    # 피자들의 치즈 상태
    ch = list(map(int, input().split()))
    # 화덕의 역할
    queue = []
    # 번호가 적힌 피자들
    idx = [i for i in range(M)]
    FIRE(N, idx)

# 테스트 케이스 출력
#1 4
#2 8
#3 6