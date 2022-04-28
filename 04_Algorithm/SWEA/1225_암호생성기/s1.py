# 1225_암호생성기
# 2022-02-25

import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T+1):

    tc = int(input())

    # 암호 리스트 받아오기
    num = list(map(int, input().split()))

    # 암호리스트의 마지막 숫자가 0이 되면 반복문 종료
    while num[-1] != 0:

        # 맨 앞의 숫자를 1~6씩 사이클을 돌리며 빼야 한다.
        for i in range(1, 6):
            temp = num[0] - i

            # 만약 temp가 0이하가 되면 암호 리스트 맨 마지막에 0을 붙인다.
            if temp <= 0:
                temp = 0
                num = num[1:] + [temp]

            # 그렇지 않다면 뺀 숫자를 맨 뒤로 보내고 다시 반복
            else:
                num = num[1:] + [temp]

    print("#{} ".format(tc), *num)
