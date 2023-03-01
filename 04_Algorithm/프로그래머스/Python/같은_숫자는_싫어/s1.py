from collections import Counter
def solution(arr):
    
    tmp = arr[0]
    answer = [tmp]
    for a in arr:
        if tmp != a:
            tmp = a
            answer.append(tmp)

    return answer