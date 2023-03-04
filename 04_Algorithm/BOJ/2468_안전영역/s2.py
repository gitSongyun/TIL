import sys
sys.stdin = open('input.txt', 'r', encoding="utf-8")

N = int(input())

location = []

for _ in range(N):
    location.append(list(map(int, input().split())))

print(location)