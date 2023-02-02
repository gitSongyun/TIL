from collections import deque


def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)

    queue = deque()
    queue.append([begin, 0])

    while queue:
        print(queue)
        start, level = queue.popleft()
        if start == target:
            answer = level
            break

        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(start)):

                    if start[j] != words[i][j]:
                        temp_cnt += 1

                if temp_cnt == 1:
                    queue.append([words[i], level + 1])
                    visited[i] = True

    return answer


# begin = "hit"
# taget = 'cog'
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
