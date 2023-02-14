import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = True
    print(start)
    if start == end:
        print('end 도착! 이제 리턴')
        return

    for i in  fm[start]:
        if not visited[i]:
            level[i] = level[start] + 1
            print('DFS 실행 할거임', start, i)
            DFS(i)
    print('여긴언제지',start)            

        

N = int(input())
start, end = map(int, input().split())

V = int(input())
fm = [[] for _ in range(N+1)]
visited = [False] * (N+1)
level = [0] * (N+1)

for i in range(V):
    p, c = map(int, input().split())
    fm[p].append(c)
    fm[c].append(p)



DFS(start)
print(level)

print(level[end] if level[end] > 0 else '-1')