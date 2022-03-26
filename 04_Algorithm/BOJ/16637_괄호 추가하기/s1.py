import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())   # 수식의 길이
    int_num = (N-1)/2  # 정수의 갯수

    # 적절히 괄호를 쳐서 연산결과가 최대가 되는 경우를 찾아야 한다.
    # 괄호를 안치는 경우, 1개치는 경우, ... N개 치는 경우를 고려 해야 할 듯
    # 정수 갯수-1 만큼 괄호를 칠 수 있다.
    arr = input()

    stack = []
    op = []

    # 연산자를 만나면
    # 종료조건은 모든 경우의 수를 다 봤을 때

    for i in arr:
        if i == '*' or i == '+' or i == '-':
            op.append(i)

        else:
            stack.append(i)

