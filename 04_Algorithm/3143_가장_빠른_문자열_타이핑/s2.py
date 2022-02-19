# 3143_가장 빠른 문자열 타이핑
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# string 갯수를 세는 함수
def length(a):

    cnt = 0
    for k in a:
        cnt += 1

    return cnt

for tc in range(1, T+1):
    # A: 입력하고자 하는 문자, B: 매크로 문자
    A, B = input().split()

    a_len = length(A) # A의 길이
    b_len = length(B) # B의 길이

    cnt = 0
    i = 0 # slicing을 할 시작점

    # Slicing으로 각 문자를 비교 할 것이기 때문에 A길이 - B길이
    while i <= (a_len-b_len):
        temp = A[i:b_len+i]

        # 만약 슬라이싱 한 A와 B가 같다면 개수를 세기 위해 +1
        if temp == B:
            cnt += 1
            i += b_len # 동일한 문자 이후 부터 다시 비교하기 위해 B의 길이만큼 더해서 시작한다.

        # 서로 같지 않다면 바로 다음 인덱스 부터 비교 해야 한다.
        else:
            i += 1

    # 입력한 횟수를 알아야 하기 때문에 다음과 같이 계산해야 한다.
    ans = a_len - (b_len- 1)*cnt
    print("#{} {}" .format(tc, ans))

    #banana
    #ana
    # 이런 경우이면... 만약 슬라이싱 한거랑 원래문자의 문자랑 같다면, 바로 그 이후에서 시작하는 것이 필요할듯




