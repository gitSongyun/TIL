# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     arr = input()
#     print(arr)

# def QuickSort(A, l, r):
#     if l < r:
#         s = partition(A, l, r)  # s = 새로운 피봇
#         QuickSort(A, l, s - 1)  # s 기준 왼쪽 정렬을 위한 재귀
#         QuickSort(A, s + 1, r)  # s 기준 오른쪽 정렬을 위한 재귀
#
# def partition(nums, l, r):
#     if l >= r:
#         return
#     print(len(nums),l, r)
#     pivot = nums[l]
#     i = l+1
#     j = r
#
#     while i <= j:
#         while i <= j and nums[i] <= pivot:
#             i += 1
#
#         while i <= j and nums[i] >= pivot:
#             j -= 1
#
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#
#     nums[l], nums[j] = nums[j], nums[l]
#
#     return j
#
# T = 1
# for tc in range(1, T + 1):
#     nums = [12, 42, 32, 14, 15]
#     QuickSort(nums, 0, len(nums) - 1)
#     print(nums)

