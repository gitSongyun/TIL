from collections import Counter

def solution(topping):
    answer = 0
    chul = Counter(topping)
    bro = {}

    for t in topping:

        if t in bro:
            bro[t] += 1
        else:
            bro[t] = 1

        chul[t] -= 1

        if chul[t] == 0:
            chul.pop(t, None)

        if len(chul) == len(bro):
            answer += 1

    return answer

# topping = [1, 2, 1, 3, 1, 4, 1, 2]