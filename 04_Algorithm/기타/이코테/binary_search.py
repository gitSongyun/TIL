### 이진탐색 구현
# N, T = 10, 7
# arr = [1, 3, 5, 7, 9, 11, 12, 13, 15, 17]

# def binary_search(arr, T, start, end):

#     if start > end:
#         return None
    
#     mid = (end + start) // 2

#     if arr[mid] == T:
#         return mid

#     elif arr[mid] > T:
#         return binary_search(arr, T, start, mid - 1)
#     else:
#         return binary_search(arr, T, mid + 1, end)

# print(binary_search(arr, T, 0, N-1))
# --------------------------------------------------------------------
### 떡볶이 떡 만들기 (파라매트릭 서치, 이진탐색 이용)
# 파라매트릭 서치 : 최적화 문제를 결정 문제로 바꾸어 해결, 특정 조건을 만족하는 가장 알맞은 값 찾기 

def search(arr, N, M, start, end, result):
    if start > end :
        return result
    
    mid = (start + end) // 2

    print(start, mid, end)
    summ = 0
    for i in arr:
        if i - mid > 0:
            summ += (i - mid) 
    print(summ, M)
    if summ == M:
        result = mid
        return result
    elif summ > M :
        result = mid
        return search(arr, N, M, mid + 1, end, result)
    elif summ < M :
        return search(arr, N, M, start, mid -1, result)

# N : 떡의 갯수, M : 손님이 원하는 길이
N, M = 4, 6
arr = [19, 15, 10, 17]

end = max(arr)
result = 0
print(search(arr, N, M, 0 , end, result))
