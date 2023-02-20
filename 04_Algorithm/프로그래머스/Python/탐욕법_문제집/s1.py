def solution(n, lost, reserve):
    answer = n

    # 안가져온 학생 수 만큼 뺀다. 
    answer -= len(lost)
    cnt = 0
    for i in reserve[:]:

        if i in lost:
            # 여벌이 있는애가 lost에 있다면, reserve와 lost에서 제외시키고
            reserve.remove(i)
            lost.remove(i)
            answer += 1
            continue



    # 오름차순으로 정렬
    lost.sort()
    reserve.sort()

    for r in reserve:
        for l in lost:
            if abs(r-l) == 1:
                lost.remove(l)
                answer += 1
                break

    return answer

# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2