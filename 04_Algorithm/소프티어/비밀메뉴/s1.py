import sys
M, N, K = map(int, sys.stdin.readline().split())
code = list(map(int, sys.stdin.readline().split()))
push_btn = list(map(int, sys.stdin.readline().split()))

answer = 'normal'

for i in range(N-M+1):
    if code == push_btn[i: i+M]:
        answer = 'secret'
    

print(answer)