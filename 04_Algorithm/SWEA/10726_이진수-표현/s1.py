# 10726_이진수표현
# 2022-03-24
import sys
sys.stdin = open('input.txt')

T= int(input())

for tc in range(1, T+1):
    # N : 몇 번재 비트까지 1인가, M : 이진수로 변환 할 값
    N, M = list(map(int, input().split()))

    # 기본값 OFF
    ans = 'OFF'

    binary = ''

    # 이진수 변환
    # N은 최대값이 30 이므로 30번 반복한다.
    for i in range(30):
        binary = str(M % 2) + binary
        M = M//2

    # 맨 오른쪽 부터 N번째 까지 슬라이싱 한다.
    binary = binary[30-N: 30]

    # 슬라이싱 한 값에 1이 몇개 인지 계산
    cnt = 0
    for i in binary:
        if i == '1':
            cnt +=1

    # 만약 1의 갯수가 N과 같다면 ON으로 변환
    if cnt == N:
        ans = 'ON'
        print("#{} {}".format(tc, ans))
    else:
        print("#{} {}".format(tc, ans))
