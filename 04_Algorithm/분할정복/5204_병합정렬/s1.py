import sys
sys.stdin = open('sample_input.txt')

def merge_sort(m):
    if len(m) <= 1:
        return m

    # 1. 분할
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    # 2. 정복 : 분할된 리스트들 병합
    return merge(left, right)


def merge(left, right):
    # print('함수에 들어오는 리스트', left, right)
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    idx = len(left) * 2
    result = [0] * (len(left)+len(right))
    i = k = 0
    j = 0
    while i < len(left) or k < len(right):
        if i < len(left) and k < len(right):
            if i < len(left) and left[i] <= right[k]:
                result[j] = left[i]
                i += 1
                j += 1

            elif k < len(right) and left[i] >= right[k]:
                result[j] = right[k]
                k += 1
                j += 1

        elif i < len(left):
            result[j] = left[i]
            j += 1
            i += 1

        elif k < len(right):
            result[j] = right[k]
            j += 1
            k += 1

        # print(result)
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 배열의 길이

    arr = list(map(int, input().split()))

    cnt = 0
    a = merge_sort(arr)
    print("#{} {} {}".format(tc, a[N//2], cnt))
