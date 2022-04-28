# 4866_괄호검사
# 2022-02-22

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):

    check = input()

    stack = []
    top = -1
    ans = 1


    for i in range(len(check)):
        # 열린 소괄호 또는 중괄호라면 append 한다.
        if check[i] == '(' or check[i] == '{':
            stack.append(check[i]) 

        # 닫힌 소괄호이고, 현재 stack의 길이가 0이거나 직전 괄호가 열린 소괄호가 아니라면 
        # 소괄호의 짝이 맞지 않다는 의미 이므로 0을 반환
        if check[i] == ')':
            if len(stack) == 0 or stack.pop() != '(':
                ans = 0
                break
        # 중괄호도 마찬가지
        if check[i] == '}':
            if len(stack) == 0 or stack.pop() != '{':
                ans = 0
                break
    # 만약 stack에 괄호가 남아 있다면 짝이 맞지 않다는 의미이므로 0반환
    if stack != []:
        ans = 0

    print("#{} {}".format(tc, ans))

