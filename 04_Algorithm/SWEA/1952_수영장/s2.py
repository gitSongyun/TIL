import sys
sys.stdin = open('sample_input.txt')

def DFS(m, ssum):
    global ans

    if m>4:
        if ans > ssum:
            ans = ssum
        return

    # 1일권
    print('1일권 탐색', m)
    DFS(m+1, ssum+plan[m]*price[0])
    print('1달권 탐색', m)
    DFS(m+1, ssum+price[1])
    print('3달권 탐색', m)
    DFS(m+3, ssum+price[2])
    print('1년권 탐색', m)
    DFS(m+12, ssum+price[3])


T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))         # 가격
    plan = [0] + list(map(int, input().split()))    # 계획

    ans = 9999999

    # 함수에 현재 달과 누적합을 보내줘야 할 듯
    DFS(1, 0)
    print(ans)