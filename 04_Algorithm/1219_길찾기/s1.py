import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):

    N, road_num = list(map(int, input().split()))

    # 두 숫자씩 끊어서 받아야 할 듯 (근데 어떻게 받는지 모르겠네)

    road_1 = [0] * 100
    road_2 = [0] * 100

    arr = list(map(int,input().split()))
    # print(arr)
    for i in range(0, len(arr), 2):
        if road_1[arr[i]] == 0:
            road_1[arr[i]] = arr[i+1]

        else:
            road_2[arr[i]] = arr[i+1]

    # [1, 4, 9, 7, 8, 6, 10, 99, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [2, 3, 5, 0, 3, 7, 0, 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    # stack = []
    # stack.append(0)
    # visited = [0] * 100

    stack = [99]
    # 도착점인 99
    # 도착점에서 시작점으로 가는게 더 빠른가?
    while stack :
        idx = stack.pop()
        for i in range(100):
            if road_1[i] == idx:
                stack.append(i)
                break

            elif road_2[i] == idx:
                stack.append(i)
                break





    print("#{} {}".format(tc, idx))

        # 어떤 리스트의 인덱스에서 값이 99인지 찾는다. road_1[i] == idx, i == idx
        # p = stack.pop()
        # road_1[p] # p는 현 위치, 값은 어디로 이동 가능한지
        #road_2[road_1[p]]






# road = [[0] * 100 for _ in range(100)]
