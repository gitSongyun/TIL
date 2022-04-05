# def merge_sort(m):
#     if len(m) <= 1:
#         return m
#
#     # 1. 분할
#     mid = len(m) // 2
#     left = m[:mid]
#     right = m[mid:]
#
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     # 2. 정복 : 분할된 리스트들 병합
#     return merge(left, right)
#
#
# def merge(left, right):
#     result = []
#
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#
#     if len(left) > 0:
#         result.extend(left)
#
#     if len(right) > 0:
#         result.extend(right)
#
#     return result
#
#
# print(merge_sort([2, 4, 5, 3, 1, 6, 7, 8]))

# def quicksort(A, lo, hi):
# 	if lo<hi:
#     	pivot=partition(lo, hi)
#         quicksort(A, lo, pivot-1)
#         quicksort(A, pivot+1, hi)
#
# def partition(lo, hi):
# 	pivot=A[hi]
#     left=lo
#     for right in range(lo, hi):
#     	if A[right]<pivot:
#         	A[left], A[right] = A[right], A[left]
#             left+=1
# 	A[left], A[hi] = A[hi], A[left]
#     return left
#
# A = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# quicksort(A, 0, len(A)-1)


def enq(v):
    global last
    last += 1
    tree[last] = v

    c = last
    p = c//2

    # 부모가 있고, 부모보다 자식이 더 작다면
    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1

    p = 1
    c = p*2

    while c <= last:
        # 오른쪽 노드가 존재하고, 오른쪽 노드가 더 작다면
        if c+1 <= last and tree[c] >= tree[c+1]:
            c += 1

        if tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2

        else:
            break


last = 1