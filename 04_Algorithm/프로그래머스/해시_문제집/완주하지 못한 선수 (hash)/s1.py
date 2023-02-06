def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    for runner in participant:
        dic[hash(runner)] = runner
        temp += int(hash(runner))

    for complete in completion:
        temp -= int(hash(complete))

    answer = dic[temp]

    return answer