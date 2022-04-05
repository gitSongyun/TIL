import sys
sys.stdin = open('sample_input.txt')



T = int(input())

for tc in range(1, T+1):

    N, M = list(map(int, input().split()))

    arr = list(map(int, input().split()))


    stack = []
    for i in range(M):
        stack = arr.pop(0)
        arr.append(stack)

    print("#{} {}".format(tc, arr[0]))