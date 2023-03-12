def solution(sizes):
    answer = 0
    maxW = 0
    maxH = 0
    
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i]) 
        if sizes[i][0] > maxW:
            maxW = sizes[i][0]
        if sizes[i][1] > maxH:
            maxH = sizes[i][1]
    answer = maxH * maxW
    return answer