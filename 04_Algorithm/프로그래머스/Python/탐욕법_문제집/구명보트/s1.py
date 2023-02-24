def solution(people, limit):
    answer = 0
    tmp_boat = 
    people.sort()
    
    l = 0
    r = len(people) - 1
    while l <= r:
        if people[l] + people[r] >= limit:
            answer += 1
            r -= 1
        else :
            r -= 1
            l += 1
    
        if r < 2:
            break

    return answer