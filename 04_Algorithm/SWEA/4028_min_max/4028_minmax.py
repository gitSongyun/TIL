# 4828_min_max 풀이
# 2022-02-10

import sys
sys.stdin=open("sample_input.txt")

T = int(input()) # Testcase

for i in range(1,T+1):
    N = int(input()) # 정수 갯수
    a_i = list(map(int, input().split())) # 정수 list 생성

    max_val = a_i[0]
    min_val = a_i[0]
    for j in a_i:
        if max_val <= j:
            max_val = j

        elif min_val > j:
            min_val = j

    ans = max_val-min_val

    print("#{} {}". format(i,ans))
