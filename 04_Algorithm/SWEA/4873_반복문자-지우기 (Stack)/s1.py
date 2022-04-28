import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    arr = list(input())
    # print(arr)
    idx = 0

    while idx < len(arr)-1:

        if len(arr) == 1:
            break



        elif arr[idx] == arr[idx+1]:
            arr.pop(idx) # 1

            arr.pop(idx) # 2

            if idx == 0:
                idx = 0

            else:
                idx -= 1

        else:
            idx += 1


    print("#{} {}".format(tc, len(arr)))


