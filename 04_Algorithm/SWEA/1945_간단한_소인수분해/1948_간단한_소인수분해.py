# 1948_간단한 소인수분해
# 2022-02-11

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))

    N = int(N[0])
    a = b = c = d = e = 0
    while N > 1:

        if not N % 2 :
            N = N / 2
            a+=1

        if not N % 3 :
            N = N / 3
            b+=1

        if not N % 5 :
            N = N / 5
            c+=1

        if not N % 7 :
            N = N / 7
            d+=1

        if not N % 11 :
            N = N / 11
            e+=1

    print('#{} {} {} {} {} {}' .format(tc, a, b, c, d, e))






