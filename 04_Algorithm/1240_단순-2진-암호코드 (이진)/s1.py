import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 행의 크기, M: 열의 크기
    N , M = list(map(int, input().split()))

    code = [list(map(int, input())) for _ in range(N)]

    # 암호 코드 dict
    bin_code = {
                 '0001101': 0, '0011001': 1, '0010011': 2,
                 '0111101': 3, '0100011': 4, '0110001': 5,
                 '0101111': 6, '0111011': 7, '0110111': 8,
                 '0001011': 9
               }

    # 코드가 들어있는 행의 마지막 값의 좌표를 담을 변수
    idx = []

    x = 0
    i = 0

    # 이 반복문에서 코드가 들어있는 행을 찾는다.
    while x != 1:

        # 코드의 마지막 부분의 좌표를 뽑는다.
        for j in range(M):
            if code[i][j] == 1:
                idx = [i, j]

                # 행을 찾았다면 반복문 종료를 위해 x를 1로 바꾼다.
                x = 1

        if x == 1:
            break
        # 1을 못찾았다면 다음 행을 탐색한다.
        i += 1

    # 코드를 arr 에 담는다.
    arr = [0] * 8
    for i in range(8):
        arr[i] = code[idx[0]][idx[1]-6-7*i:idx[1]+1-7*i]

    check = 0   # check = 유효한 코드 인지 (10의 변수인지) 확인하는 변수
    sum_c = 0   # sum_c = 유효한 코드 인 경우 코드의 합을 담을 변수
    for i in range(8):

        # 리스트 형태의 arr 에서 str 형태의 result 로 변환
        # [0, 1, 1, 1, 0, 1, 1] => 0111011
        result = ''.join(map(str, arr[i]))

        # 코드의 합을 계산한다.
        sum_c += bin_code[result]

        # 짝수번째 자리라면 곱하기 3을 한다.
        if i % 2:
            check += bin_code[result]*3

        # 홀수번째 자리라면 그냥 더한다.
        else:
            check += bin_code[result]

    # 만약 10의 배수 이면 코드의 합을 출력한다.
    if not check % 10:
        print("#{} {}".format(tc, sum_c))

    # 10의 배수가 아니라면 0을 출력한다.
    else:
        print("#{} {}".format(tc, 0))




