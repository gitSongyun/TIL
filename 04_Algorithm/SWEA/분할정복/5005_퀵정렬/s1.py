# import sys
# sys.stdin = open('sample_input.txt')
#
#
# def hoare(A, l, r):
#     p = A[l]    # 피봇
#     i, j = l, r
#
#     # i와 j가 교차하기 전까지 반복
#     while i <= j:
#         # i번 인덱스가 피벗보다 큰 값을 찾았고,
#         # j번 인덱스가 피벗보다 작은 값을 찾을 때 까지 반복
#
#         # i번 인덱스가 p보다 작다면 1씩 늘린다.
#         while i <= j and A[i] <= p:
#             i += 1
#         # j번 인덱스가 p보다 크다면 1씩 줄인다.
#         while i <= j and A[j] >= p:
#             j -= 1
#
#         # i번 값과 j번 값의 자리를 바꾼다.
#         if i < j:
#             A[i], A[j] = A[j], A[i]
#
#     #
#     A[l], A[j] = A[j], A[l]
#
#     return j
#
# def quick(A, l, r):
#     # left 가 right 왼쪽에 있다면
#     if l < r:
#         s = hoare(A, l, r)
#         quick(A, l, s - 1)
#         quick(A, s + 1, r)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     arr = list(map(int, input().split()))
#
#     quick(arr, 0, len(arr)-1)
#
#     print("#{} {}".format(tc, arr[N//2]))

# 5005_퀵정렬
# 2022-03-31

def QuickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)  # s = 새로운 피봇
        QuickSort(A, l, s - 1)  # s 기준 왼쪽 정렬을 위한 재귀
        QuickSort(A, s + 1, r)  # s 기준 오른쪽 정렬을 위한 재귀


def partition(A, l, r):
    if l >= r:
        return

    print(len(A), l, r)
    pivot = A[l]  # 피봇값
    i = l + 1  # 피봇의 왼쪽 인덱스부터 탐색
    j = r  # 피봇의 오른쪽 인덱스부터 탐색

    while i <= j:
        # 피봇보다 큰 값이 나올 때까지 i 증가
        while i <= j and A[i] <= pivot:
            i += 1

        # 피봇보다 작은 값이 나올 때까지 j 감소
        while i <= j and A[j] >= pivot:
            j -= 1

        # i와 j의 자리를 바꾼다.
        if i < j:
            A[i], A[j] = A[j], A[i]

    # 위 반복문이 끝나면 피벗과 j의 자리를 교환한다.
    A[l], A[j] = A[j], A[l]

    # 피봇을 반환
    return j


T = 1
for tc in range(1, T + 1):
    nums = [12, 42, 32, 14, 15]
    QuickSort(nums, 0, len(nums) - 1)
    print(nums)