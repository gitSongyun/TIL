# 3143_가장 빠른 문자열 타이핑
# 2022-02-17

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def my_len(a):

    cnt = 0
    for k in a:
        cnt += 1

    return cnt


for tc in range(1, T+1):
    A, B = input().split()

    a_len = my_len(A)
    b_len = my_len(B)

    # A의 글자수에서 B 문자열과 겹치는 게 몇번인지 세면 몇 번 만에 타이핑 칠 수 있을지 나올듯
    # 아 힘들다

    cnt = 0
    for i in range(a_len-b_len+1):
        temp = A[i:b_len+i]

        if temp == B:
            cnt += 1

    print(cnt)
    ans = a_len - (b_len- 1)*cnt
    print("#{} {}" .format(tc, ans))

    #banana
    #ana
    # 이런 경우이면... 만약 슬라이싱 한거랑 원래문자의 문자랑 같다면, 바로 그 이후에서 시작하는 것이 필요할듯

# 강서 명지 하단



