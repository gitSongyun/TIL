import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())

    binary = ''  # 이진 변환 스트링
    x = 1        # 지수
    cnt = 0      # 12자리 이하 인지 확인 할 변수
    while N > 0:

        # 2^-x 가 N 보다 크다면 0을 추가한다.
        if N < 2**-x:
            binary += '0'

        # 2^-x 가 N 보다 작다면 1을 추가한다.
        else:
            N -= 2**-x
            binary += '1'

        # 자리수 +1을 한다.
        cnt += 1
        # 지수 +1 을 한다.
        x += 1

    # 만약 13자리 이상이라면 overflow
    if cnt > 12:
        print("#{} {}".format(tc, 'overflow'))
    else:
        print("#{} {}".format(tc, binary))
