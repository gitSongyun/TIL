import sys
sys.stdin = open('sample_input.txt')


def check(p):
    run_p = 0
    # run 찾기
    for j in range(7):
        sum_r1 = 0
        for k in p1[1 + j: 4 + j]:
            sum_r1 += k
            if sum_r1 == 3:
                run_p += 1

T = int(input())

for tc in range(1, T+1):

    arr = list(map(int, input().split()))

    p1 = [0] * 10
    p2 = [0] * 10

    run_p2 = 0
    for i in range(len(arr)):

        # 짝수
        if not i%2:
            p1[arr[i]] += 1
            check(p1)
        else:
            p2[arr[i]] += 1
            check(p2)





