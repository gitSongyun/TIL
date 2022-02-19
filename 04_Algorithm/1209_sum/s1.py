# 1209_sum
# 2022-02-15

import sys
sys.stdin=open('input.txt')

T = 10

for tc in range(1, T+1):

    N= int(input()) # Test case 번호

    # 100X100 행렬을 담을 list 생성 
    arr=[]
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 정방 행렬이므로 행,열 갯수 동일
    col_num = row_num = len(arr)

    # 행, 열, 대각선 합을 담을 리스트 및 합 초기화
    sum_row=[]
    sum_col=[]
    sum_d_l=0 # 왼쪽에서 시작하는 대각선의 합
    sum_d_r=0 # 오른쪽에서 시작하는 대각선의 합
    
    for i in range(len(arr)):
        sum_d_l += arr[i][i] 
        sum_d_r += arr[i][len(arr)-1-i]
        # 각 행 및 열의 합을 각각 담아야 하므로 두 번째 반복문이 돌 때 마다 sum_r(c)을 초기화 한다.
        sum_r = 0
        sum_c = 0
        for j in range(len(arr)):
            sum_r+=arr[i][j]
            sum_c+=arr[j][i]
        sum_row.append(sum_r) # 행 합
        sum_col.append(sum_c) # 열 합
    
    # 행의 합, 열의 합중 큰 값을 뽑아 내야 함
    # sum_row 에 sum_col을 더해 하나의 리스트로 만들어 그 중 최대값 뽑아낸다.
    sum_row += sum_col
    max_rc = sum_row[0] # 기준값
    for k in sum_row:
        if max_rc < k :
            max_rc = k
    
    # 두 대각선의 합 중 최고값 가려냄
    if sum_d_l >= sum_d_r:
        max_dlr = sum_d_l
    else:
        max_dlr = sum_d_r
    
    # 각 행렬의 합과 대각선 합 을 비교해 결과 출력
    if max_rc >= max_dlr:
        print("#{} {}" .format(tc, max_rc))
    else:
        print("#{} {}" .format(tc, max_dlr))


