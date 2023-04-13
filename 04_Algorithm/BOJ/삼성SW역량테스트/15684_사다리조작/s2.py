import sys
sys.stdin = open('input.txt')

# 사다리에 가로선을 놓는 함수
def dfs(start, cnt):
    global res
    if cnt == min_cnt:
        if check():
            res = cnt
        return
    for i in range(start, h):
        for j in range(n-1):
            # ij 위치에 사다리가 있지 않고, 전후로도 사다리가 없으면
            print(i,j, ladder[i][j-1])
            if not ladder[i][j-1] + ladder[i][j] + ladder[i][j+1]:
                # 사다리 놓기
                ladder[i][j] = 1
                dfs(i, cnt+1)
                # 함수 재귀 끝나면 사다리 다시 빼기(원상복구)
                ladder[i][j] = 0

# 사다리 가로선 추가 후, 모든 세로선이 자기 번호로 내려오는 지 확인하는 함수
def check():
    # h행 n열, 1열부터 시작
    for j in range(n):
        tmp = j
        for i in range(h):
            if ladder[i][tmp]: # 이어져 있으면 오른쪽으로 열 한칸 이동
                tmp += 1
            elif ladder[i][tmp-1]: # 왼쪽방향이 이어져 있는 지 확인
                tmp -= 1 # 왼쪽으로 열 이동

        # 모든 행을 거친 뒤 자기 원래 열 번호(j)로 돌아오지 않으면 False
        if tmp != j:
            return False
    # 모든 열이 사다리를 타고 자기 열 번호로 돌아온다면 True 반환
    return True

n, m, h = map(int, input().split())
ladder = [[0]*n for _ in range(h)]
for i in range(m):
    # a 행 b 열
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

ladder[0][-1] = 9
print(ladder)
res = 10000
for min_cnt in range(4):
    dfs(0, 0)
    if res != 10000:
        print(res) # 최솟값 출력
        break
else:
    print(-1) # 불가능한 경우, cnt가 4이상인 경우 -1 출력