import sys
sys.stdin = open('input.txt')

n = int(input())
member = list(map(int, input().split()))

# 멤버 오름차순 정렬
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left_list, pivot_list, right_list = [], [pivot], []
#     for num in arr:
#         if num > pivot:
#             right_list.append(num)
#         elif num < pivot:
#             left_list.append(num)
#     # print(pivot, left_list, right_list)
#     return quick_sort(left_list) + pivot_list + quick_sort(right_list)

# new_member = quick_sort(member)
member.sort()

ans = member[0] + member[-1]
# 양끝 더하기
for i in range(len(member)//2+1):
    # print(i)
    sum = member[i] + member[-i-1]
    # print(sum)
    if ans > sum:
        ans = sum

# 그 중 최소값이 답이다.
print(ans)

