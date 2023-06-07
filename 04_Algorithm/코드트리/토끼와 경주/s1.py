import sys
sys.stdin = open('input.txt')

def init(q):
    global K, M, P
    K, M, P = q[1:4]

    for i in range(P):
        rabbit.append(q[4+2*i:6+2*i])
        for j in range(5):
            rabbit[i].append(0)

def race():
    # K번 반복
    # 우선순위 대로 토끼 선정하기
    # 우선순위: 점프횟수 -> 행+열 작은 -> 행 작은 -> 열 작은 -> 고유번호 작은
    # 점프횟수 최저 값 토끼 찾기
    pass

def changeDist():
    pass

def selectBest():
    pass
import heapq
Q = int(input())
K, M, P = 0, 0, 0
rabbit = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 100:
        init(query)

    # 경주 진행
    elif query[0] == 200:
        race(query)


    # 이동거리 변경
    elif query[0] == 300:
        changeDist(query)


    # 최고의 토끼 선정
    else:
        selectBest(query)


# 토끼는 [뛴 횟수, 행+열정보, 행정보, 열정보, 고유번호, 거리, 점수] 를 가짐

# 100 명령이면 토끼 정보 갱신
# [10, 2, 0, 0, 0, 0, 0] 토끼 10
# [20, 5, 0, 0, 0, 0, 0] 토끼 20



