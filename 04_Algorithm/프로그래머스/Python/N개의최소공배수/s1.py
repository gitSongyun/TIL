import math

def lcm(a, b):
    return int( a * b / math.gcd(a, b))


def solution(arr):
    answer = 0

    stk = []

    for el in arr:
        if not stk:
            stk.append(el)
        else:
            print(stk, el)
            stk.append(lcm(stk.pop(), el))
            print(stk)
    return stk[-1]