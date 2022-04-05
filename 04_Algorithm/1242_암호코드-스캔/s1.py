import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 행의 크기, M: 열의 크기
    N , M = list(map(int, input().split()))

    code = [input() for _ in range(N)]
    print(code)

    for i in range(N):
        for j in range(M):
            if code[i][j] !=0:






    # for i in range(N):
    #     code[i] = code[i].strip('0')
    #
    # code = set(code)
    # code = list(code)
    #
    # ans = []
    # for i in range(len(code)):
    #     if code[i]:
    #        ans.append(code[i])
    # # print(ans)



        # for j in range(M):



    # 코드의 시작, 끝 좌표를 얻은 다음 그 사이의 값을 슬라이스로 다 가져와야 할 듯

    # x = 0
    # while x != 1:
    #
    #     for i in range(N):
    #         for j in range(M):
    #
    #             if code[i][j] != 0:
    #                 while

    # 길이가 56이라면 위에거 그대로 써도 되는데
    # 112 이상이라면 비율로 봐야 한다.




    # 암호 코드 dict
    # bin_code = {
    #              '0001101': 0, '0011001': 1, '0010011': 2,
    #              '0111101': 3, '0100011': 4, '0110001': 5,
    #              '0101111': 6, '0111011': 7, '0110111': 8,
    #              '0001011': 9
    #            }


