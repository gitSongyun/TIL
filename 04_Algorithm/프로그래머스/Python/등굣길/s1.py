def solution(m, n, puddles):
    answer = 0

    for p in puddles:
        p[0], p[1] = p[1], p[0]

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 1 and j == 1:
                continue

            elif [i, j] in puddles:
                dp[i][j] = 0

            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007

    for d in dp:
        print(d)

    return dp[n][m]