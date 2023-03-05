def solution(brown, yellow):
    answer = []
    summ = brown + yellow
    visited = []

    for i in range(1, summ+1):
        x = sorted([i, summ // i], reverse=True)
        if (x[0]-2)*(x[1]-2) == yellow:
            answer.append(x)
            break
            
    return answer[-1]