import sys
sys.stdin = open('input.txt')


def dfs(d_sum, depth):
    global max_ans
    global min_ans
    # 종료조건, 수의 갯수 이상이 되면 종료
    if depth == N:
        max_ans = max(max_ans, d_sum)
        min_ans = min(min_ans, d_sum)
        return

    # 더하기
    if p_list[0] > 0:
        p_list[0] -= 1
        dfs(d_sum + nums_list[depth], depth + 1)
        p_list[0] += 1

    # 빼기
    if p_list[1] > 0:
        p_list[1] -= 1
        dfs(d_sum - nums_list[depth], depth + 1)
        p_list[1] += 1

    # 곱하기
    if p_list[2] > 0:
        p_list[2] -= 1
        dfs(d_sum * nums_list[depth], depth + 1)
        p_list[2] += 1

    # 나누기
    if p_list[3] > 0:
        tmp = abs(d_sum) // nums_list[depth]

        if d_sum < 0:
            tmp *= -1

        p_list[3] -= 1
        dfs(tmp, depth + 1)
        p_list[3] += 1


N = int(input())
nums_list = list(map(int, input().split()))
p_list = list(map(int, input().split()))
max_ans = int(-1e9)
min_ans = int(1e9)
depth = 1

dfs(nums_list[0], depth)
print(max_ans)
print(min_ans)
