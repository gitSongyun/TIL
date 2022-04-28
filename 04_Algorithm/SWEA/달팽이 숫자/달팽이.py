# # (0,0)~(0,4). (1,4)~(4,4), (4,3)~(4,0) (3,0)~(1,0)


# arr_2 = [[9, 20, 2, 18, 11],
#      [19, 1, 25, 3, 21],
#      [8, 24, 10, 17, 7],
#      [15, 4, 16, 5, 6],
#      [12, 13, 22, 23, 14]]

# N = M = 5

# # 2차원 리스트를 1차원 리스트로 만들자
# arr_1 = []
# for row in range(N):
#     for col in range(N):
#         arr_1.append(arr_2[row][col])
# # [9, 20, 2, 18, 11, 19, 1, 25, 3, 32, 8, 24, 10, 17, 7, 15, 4, 16, 5, 6, 12, 13, 22, 23, 14]

# # 셀렉션 정렬
# for a in range((N*M)-1):
#     minIdx = a
#     for b in range(a+1, 25):
#         if arr_1[minIdx] >= arr_1[b]:
#             minIdx = b

#     arr_1[a], arr_1[minIdx] = arr_1[minIdx], arr_1[a]

# # 달팽이 정렬
# temp = [0] * 25
# cnt=0
# while cnt < N:

#     if cnt % 2:
#     # 열이 움직임
#     g=0
#     for j in range (N):
#          temp[g][j]=arr_1[j] #0,0 ~ 0,4 / 4,3 ~ 4,0
#     g+=1

#     if not cnt % 2:
#     s=1
#     # 행이 움직임
#     for i in range(s, N):
#         j+=1
#         temp[i][s]=arr_1[j] #1,4 ~ 4,4 / 3,0 ~ 1,0
#     s+=1

#     cnt+=1
# [0,0 ~ 0,4] [1,4 ~ 4,4] , [4,3 ~4,0], [3,0 ~1,0], [1,1~1,3] [2,3 ~ 3,3]
# while로
# cnt = 0
# while cnt < 9 :
#
#     # 행에서 움직이는 친구
#     a=0
#     for i in range(a,N):
#
#         for
#         arr[a][i]

    # for i in range(N):
    #
    # for j in range(N-1):
    #         if a[i][j] < a[minIdx]:
    #             minIdx = a[i]

# 셀렉트 정렬
# for i in range(N-1):
#     minIdx = i
#     for j in range(i+1, N):
#         if a[minIdx] > a[j]:
#             minIDX = j
#     a[i], a[minIDX] = a[minIdx], a[i]

# 승초리 코드
import random

nums = [_ for _ in range(1, 26)]    # 1-25 숫자 생성
arr = [[0] * 5 for _ in range(5)]   # 배열 생성
random.shuffle(nums)                # 숫자 섞기
arr_1 = list()                      # 1차원 배열
cnt = 0

# 2차원 배열 만들기 for what? maybe for input?
for n in range(5):
    for m in range(5):
        arr[n][m] = nums[cnt]
        cnt += 1

# 1차원 배열 만들기 for what? maybe for sort?
for i in range(5):
    for j in range(5):
        arr_1.append(arr[i][j])
        arr[i][j] = 0


# 정렬하기
for i in range(25):
    for j in range(i, 25):
        if arr_1[i] >= arr_1[j]:
            arr_1[i], arr_1[j] = arr_1[j], arr_1[i]

# 달팽이로 집어넣자 !
dr = [1, 0, -1, 0]    # 하 우 상 좌 (행)
dc = [0, -1, 0, 1]    # 하 우 상 좌 (열)
direction = 0
cc = 4
cr = 0

# 5 4 4 3 3 2 2 1 1
for k in range(5, 0, -1):
    if k == 5:
        for p in range(5):
            arr[0][p] = arr_1.pop(0)
        continue

    # 4 3 2 1 은 2번씩 !
    a = 0
    while a < 2:
        # 4 3 2 1
        for q in range(k):
            cc += dc[direction]
            cr += dr[direction]
            arr[cr][cc] = arr_1.pop(0)

        # 위치 변수 초기화
        if direction == 3:
            direction = 0
        else:
            direction += 1

        a += 1

    print(arr)
