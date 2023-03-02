def solution(progresses, speeds):
    answer = []
    p_len = len(progresses)
    
    day = []
    
    for i in range(p_len):
        # 작업 일 계산
        rest = 100 - progresses[i]
        x = rest // speeds[i]
        # 반올림
        if rest % speeds[i]:
            x += 1
        day.append(x)
    
    tmp = 0
    # 뒤에 만나는 값이 작은 값이면 +1, 큰 값이면 1 append
    for d in day:
        if tmp < d:
            answer.append(1)
            tmp = d
        else:
            answer[-1] += 1
    
        
    return answer