import sys
sys.stdin = open('input.txt')

import math
N = int(input())
testRoom = list(map(int, input().split()))
M, S = map(int, input().split())
answer = 0

# print(math.ceil(3/2))
for i in testRoom:
    if i <= M :
        answer += 1
        
    else :
        i -= M
        answer += 1

        if i < S :
            answer += 1
        else:
            answer += math.ceil(i/S) 
print(answer)