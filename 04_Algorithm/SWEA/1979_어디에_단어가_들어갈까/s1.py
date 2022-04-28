# 1979_어디에 단어가 들어갈 수 있을까
# 2022-02-19

import sys
sys.stdin = open('input.txt')

T = int(input())

# 리스트를 받아 행렬에 K 길이의 빈칸이 몇 개가 있는지 계산하는 함수
def find(list):
    ans = 0 # K 길이의 빈칸이 몇 개 있는지 담을 변수

    # 행 탐색
    for i in range(N):
        # 새롭운 행을 탐색할 때 마다 카운트 초기화
        cnt = 0
        for j in range(N):
            # 만약 1을 만나면 카운트 +1
            if list[i][j] == 1:
                cnt += 1

                # 카운트가 K가 되면 ans + 1
                if cnt == K:
                    ans += 1

                # 만약 K길이 이상으로 cnt가 되면 ans - 1 해서 되돌려주고, cnt 초기화 ex) 0 1 1 1 1
                if cnt > K:
                    ans -= 1
                    cnt = 0
            # 0을 만나면 cnt 초기화
            else:
                cnt = 0

    return ans



for tc in range(1, T+1):
    # N = 가로세로 길이, K = 단어의 길이
    N, K = map(int,input().split())

    # 단어 퍼즐을 받을 리스트
    arr= []
    # 2차원 행렬로 받음
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    row_num = find(arr) # 행에서 K길이의 글자가 들어갈 빈칸의 갯수

    # 전치행렬 변환
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


    col_num = find(arr) # 열에서 K길이의 글자가 들어갈 빈칸의 갯수

    result = row_num + col_num # 최종 결과

    print("#{} {}".format(tc, result))