import sys
sys.stdin = open('input.txt')


N = int(input()) # 전구 갯수
arr = list(map(int, input().split()))
num = int(input())

for i in range(num):
    std = list(map(int, input().split()))

    # 남자는 카드의 배수 만큼 숫자를 바꾼다.
    if std[0] == 1:
        # 0 1 0 1 0 0 0 1
        # 3-1 번과 3*2-1번을 바꾼다.
        for j in range(std[1]-1, len(arr), std[1]): # 3, 6,
            arr[j] = int(not(arr[j]))

    # 여자는 카드에 해당하는 인덱스에서 양쪽을 비교한다.
    elif std[0] == 2:
        arr[std[1]-1] = int(not(arr[std[-1]-1]))

        # 만약 양쪽에 값이 같은 값이면 반대로 바꾼다.
        j = 1
        while 0 <= std[1] -1 - j < N and 0 <= std[1] - 1 + j < N:
            if arr[std[1]-1-j] == arr[std[1]-1+j]:

                arr[std[1]-j-1] = int(not(arr[std[1]-j-1]))
                arr[std[1]+j-1] = int(not(arr[std[1]+j-1]))

            else:
                break

            j += 1

k = 0
while k < len(arr):

    if k % 20 == 19:
        print(arr[k])
        k += 1
    else:
        print(arr[k], end=' ')
        k += 1






