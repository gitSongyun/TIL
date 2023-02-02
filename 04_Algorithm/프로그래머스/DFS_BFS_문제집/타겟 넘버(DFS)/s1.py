def solution(numbers, target):
    global answer
    answer = 0

    def dfs(idx, result):

        if result == target:
            global answer
            answer += 1
            return

        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)

    return answer





# numbers =  [4, 1, 2, 1]
# target = 4