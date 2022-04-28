# 1216_회문2 풀이
# 2022-Py-ch
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):

    N = int(input()) # 테스트 케이스 번호

    arr1 = []
    arr2 = []

    # 입력 행렬을 받아온다.
    for _ in range(100):
        arr1.append(list(input()))

    # 열에서 회문을 찾기 위한 전치행렬을 만든다.
    arr2 = [[0]*100 for _ in range(100)]

    for a in range(100):
        for b in range(100):
            arr2[a][b] = arr1[b][a]

    max_1 = 0 # 행에서 찾은 회문의 최대길이
    max_2 = 0 # 열에서 찾은 회문의 최대길이

    for i in range(0, 100):
        for j in range(0, 100):
            # 슬라이싱 범위를 하나씩 늘려 갈거다
            # 시작위치를 한칸씩 옮기기 위해 z를 이용한다.
            for z in range(100):
                temp_1 = arr1[i][z:z+j+1] # 가로
                temp_2 = arr2[i][z:z+j+1] # 전치행렬

                # 행에서 회문을 찾고 최고 길이를 찾는다.
                if temp_1 == temp_1[::-1]:
                    if max_1 < len(temp_1):
                        max_1 = len(temp_1)
                        break

                # 열에서 회문을 찾고 최고 길이를 찾는다.
                if temp_2 == temp_2[::-1]:
                    if max_2 < len(temp_2):
                        max_2 = len(temp_2)
                        break

    if max_1 > max_2:
        print("#{} {}".format(tc, max_1))
    else:
        print("#{} {}".format(tc, max_2))

    # 고지식한 방법
    # 99번째 행까지 탐색하고, 반복문 끝낼거야~
    # i = 0
    # while i < 100:
    #     r = 0
    #     for c in range(r + 1, 100):
    #         #  고정 값,       탐색 값
    #         if arr[i][r] == arr[i][c]:
    #             for j in range((r-c)//2):
    #                 if arr[i][r+1] == arr[i][c-1]:
    #                     cnt += 1


