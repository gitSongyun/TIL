import sys
sys.stdin = open('input.txt')

N = int(input())
rope = [int(input()) for _ in range(N)]

rope.sort(reverse=True)

result = []
for i in range(N):
    result.append(rope[i] * (i+1))

print(max(result))