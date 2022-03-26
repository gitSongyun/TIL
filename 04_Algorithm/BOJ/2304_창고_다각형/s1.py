import sys
sys.stdin = open('input.txt')

N = int(input()) # 기둥의 갯수

arr = [list(map(int,input().split())) for _ in range(N)]

# 순서대로 기둥 정렬
for i in range(N-1):
    for j in range(N-1):
        if arr[i][0] < arr[j][0]:
            arr[i], arr[j] = arr[j], arr[i]






# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [15, 8], [13, 6]]

for i in range(N):

max_1 = 0
# for n in range(N):