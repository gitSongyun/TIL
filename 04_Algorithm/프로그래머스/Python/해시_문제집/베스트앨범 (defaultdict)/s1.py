from collections import defaultdict


def solution(genres, plays):
    answer = []
    # key = 장르, value = 재생횟수 lis 를 할당할 dict
    hash_map = defaultdict(list)
    # 장르별 재생횟수의 합을 할당 할 dict
    hash_sum = {}

    # dict들에 값을 할당 해준다.
    for i in range(len(genres)):
        if genres[i] in hash_sum:
            hash_sum[genres[i]] += plays[i]
        else:
            hash_sum[genres[i]] = plays[i]

        hash_map[genres[i]].append(plays[i])

    # 장르별 재생횟수를 내림차순으로 정렬
    hash_sum = sorted(hash_sum.items(), key=lambda x: x[1], reverse=True)

    # 재생횟수가 많은 순서대로 장르를 하나씩 넘겨준다.
    for genre, cnt in hash_sum:
        # 장르별 노래의 재생횟수를 내림 차순으로 정렬
        hash_map[genre].sort(reverse=True)

        # 최대 두개만 넣을 수 있기 때문에 2번 반복
        for i in range(2):
            # 정렬된 횟수와 genre를 비교하기 위한 idx
            idx = plays.index(hash_map[genre][i])
            # 같은 곡을 두번 넣을 수 있기 때문에 초기화
            plays[idx] = 0
            # 장르별 노래의 갯수가 2개 미만이라면 그 곡만 넣고 반복문 종료
            if len(hash_map[genre]) < 2:
                answer.append(idx)
                break
            # 재생횟수와 장르가 일치한다면
            if genres[idx] == genre:
                # 그 장르의 idx를 답에 넣는다.
                answer.append(idx)

    return answer

# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]