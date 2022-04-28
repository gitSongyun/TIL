# 4835_구간합 풀이
# 2022-02-10

import sys

sys.stdin = open("sample_input.txt")


T = int(input())

for i in range(1, T+1):
    # N,M은 '10 3' 이렇게 넘어오므로
    N,M = map(int, input().split()) # N=정수의 갯수, M=구간의 갯수
    a = list(map(int,input().split())) # 정수 list
    R = N-M+1 # 구간합의 갯수
    sum_a = [0] * R # 구간합을 담을 list 생성

    # R(N-M+1)번 만큼 반복 해야 함.
    for j in range(R):
        for z in range(M): # 구간의 개수 만큼 반복
            sum_a[j] += a[j+z] # 더한 값을 sum_a에 저장, [0] [1] [2] 더하고, [1] [2] [3] 더하고
        
        max_val = sum_a[0]
        min_val = sum_a[0]
        
        # sum_a list에서 최대값과 최소값 구별
        for k in range(len(sum_a)):
            if sum_a[k] >= max_val:
                max_val = sum_a[k]

            elif sum_a[k] < min_val:
                min_val = sum_a[k]

    ans = max_val-min_val # 최대값 최소값 차
    print("#{} {}" .format(i, ans))



