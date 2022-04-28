# 4869_종이붙이기 풀이
# 2022-02-22
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):

    N = int(input())

    # 밑변의 길이가 10씩 늘어남에 따라 특정한 규칙을 가지게 된다. 
    for i in range(N//10): 

        if i == 0:
            temp = [1]

        elif i % 2:
            temp.append(temp[i-1] * 2 +1)

        else:
            temp.append(temp[i-1] * 2 -1)

    ans = temp.pop()
    print("#{} {}" .format(tc, ans))