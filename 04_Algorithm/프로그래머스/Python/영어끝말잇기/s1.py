def solution(n, words):
    answer = [0, 0]
    w = [words[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    tmp = words[0]
    
    for i in range(1, len(words)):
        
        # 올바른 단어인지 판단 (끝말, 중복x) 
        if tmp[-1] == words[i][0] and words[i] not in w:
            tmp = words[i]
            w.append(words[i])

        else :
            who = i % n + 1
            cycle = i // n + 1
            answer[0] = who
            answer[1] = cycle
            break

    return answer