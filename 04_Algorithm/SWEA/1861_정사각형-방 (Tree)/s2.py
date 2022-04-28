import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    edge = [[] for _ in range(N**2 + 1)]